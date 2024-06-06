import streamlit as st
import pytz
from page_config import switch_page
from components.button import Button
from components.fields import TextField, PasswordField
from auth import try_login

st.set_page_config(page_title="CRM", page_icon="./img/logo_pernexium.png", layout="wide")

#TODO: GENERALIZAR
st.session_state.roles = ['admin', 'supervisor', 'agente']

def render():

    if st.session_state.get('logged_in'):
        switch_page('home')

    if st.session_state.get('redirected_to_login'):
        st.toast("Debes iniciar sesión para acceder a esta página.")
        st.session_state['redirected_to_login'] = False
    
    st.header("Base App")


        
    correo = TextField("correo_inicio_sesion", "Correo", "", st, border = False)

    password = PasswordField("password_inicio_sesion", "Contraseña", "", st, border = False)


    if Button(None, "Login", None, "primary"):
        login()

def login():

    correo = st.session_state.get("correo_inicio_sesion")
    password = st.session_state.get("password_inicio_sesion")
    
    try_login(correo, password)

    if st.session_state.get('logged_in'):
        switch_page('home')


render()