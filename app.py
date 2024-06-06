import streamlit as st
import pytz
from page_config import switch_page
from components.button import Button
from components.fields import TextField, PasswordField
from utils import hash_password, get_engine
from sqlalchemy import text

st.set_page_config(page_title="CRM", page_icon="./img/logo_pernexium.png", layout="wide")

st.session_state.roles = ['admin', 'supervisor', 'agente']

def render():
    parent = st
    if st.session_state.get('logged_in'):
        switch_page('home')

    if st.session_state.get('redirected_to_login'):
        st.toast("Debes iniciar sesión para acceder a esta página.")
        st.session_state['redirected_to_login'] = False
    
    st.header("Base App")
    
    correo = TextField("correo_inicio_sesion", "Correo", "", parent, border = False)

    password = PasswordField("password_inicio_sesion", "Contraseña", "", parent, border = False)

    if Button(None, "Login", None, "primary"):
        login()

def login():
    """
    st.session_state['logged_in'] = dict(
        agent_id = "1",
        agent_name = "Juan Pérez",
        agent_role = "Administrador"
    )
    switch_page('home')
    """
    
    correo = st.session_state.get("correo_inicio_sesion")
    password = st.session_state.get("password_inicio_sesion")
    
    if correo and password:
            # Hashear la contraseña ingresada
            hashed_password = hash_password(password)
            # Conectar a la base de datos
            engine = get_engine()
            with engine.connect() as connection:
                # Consulta para obtener el hash de la contraseña asociada al correo electrónico
                query = text("SELECT user_id, name, pass, role FROM users WHERE email = :email")
                result = connection.execute(query, {"email": correo})
                user = result.fetchone()
                # Verificar si el usuario existe y la contraseña es correcta
                if user and hashed_password == user["pass"]:
                    st.success("Inicio de sesión exitoso.")
                    st.session_state['logged_in'] = dict(
                        agent_id = user['user_id'],
                        agent_name = user['name'],
                        agent_role = user['role']
                    )
                    st.toast("Inicio de sesión exitoso.")
                    switch_page('home')
                    
                else:
                    st.error("Correo electrónico o contraseña incorrectos.")
                    
    else:
        st.error("Correo electrónico o contraseña incorrectos.")


render()