import streamlit as st
from components.fields import TextField, PasswordField, SelectField
from components.br import BR
from components.button import Button
from page_config import inject_navbar, require_login
from sqlalchemy import create_engine, text
from utils import hash_password, get_engine
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

st.set_page_config(page_title="CRM - Registro Usuario", page_icon="./img/logo_pernexium.png", layout="wide")
if 'campaigns_dict' not in st.session_state:
    st.session_state.campaigns_dict = None

@inject_navbar
@require_login
def render(parent = st):
    if st.session_state.campaigns_dict == None:
        st.session_state.campaigns_dict = get_campaings_name()
        
    parent.header("Registro de Usuario")

    with parent.container(border = True):

        _, fieldset, _ = parent.columns([1, 6, 1])

        with fieldset:
            BR(2, parent)

            nombre = TextField("nombre_registro_usuario", "Nombre", "", parent, border = False)
  
            correo = TextField("correo_registro_usuario", "Correo", "", parent, border = False)
    
            campania = SelectField("select_campaing", "Campaña", st.session_state.campaigns_dict.keys(), parent = st, border = False)
        
            rol = SelectField("select_rol", "Rol", st.session_state.roles, parent = st, border = False)

            password = PasswordField("password_registro_usuario", "Contraseña", "", parent, border = False)

            password_ver = PasswordField("password_ver_registro_usuario", "Verificar Contraseña", "", parent, border = False)

            BR(2, parent)
            
            Button("registrar_usuario", "Registrar", handle_registrar, "primary", parent)


def get_campaings_name():
  
    engine = get_engine()

    query = "SELECT campaign_id, name FROM campaigns"
    dict_names = {}
    with engine.connect() as connection:
        result = connection.execute(query)
        for row in result:
            dict_names[row['name']] = row['campaign_id']

    return dict_names


def insert_user(nombre, correo, password, campaign_id, role):
    engine = get_engine()
    insert_query = text("INSERT INTO users (campaign_id, name, email, pass, role) VALUES (:campaign_id, :nombre, :correo, :password, :role)")
    
    try:
        with engine.connect() as connection:
            connection.execute(insert_query, {"campaign_id": campaign_id, "nombre": nombre, "correo": correo, "password": password, "role": role})
        st.toast("Usuario registrado con éxito")
    except IntegrityError as e:
        st.toast("Error al insertar el usuario: El correo ya existe.")
    except SQLAlchemyError as e:
        st.toast(f"Error al insertar el usuario: {e}")
            
            
            
def handle_registrar():
    print("REGISTRO DE DATOS")

    nombre = st.session_state.get("nombre_registro_usuario")
    correo = st.session_state.get("correo_registro_usuario")
    rol = st.session_state.get("select_rol")
    password = st.session_state.get("password_registro_usuario")
    campaign_name = st.session_state.get("select_campaing")
    password_ver = st.session_state.get("password_ver_registro_usuario")

    if not nombre or not correo or not password or not password_ver:
        st.error("Debes llenar todos los campos")
        return
    
    if password != password_ver:
        st.error("Las contraseñas no coinciden")
        return
    
    insert_user(nombre, correo, hash_password(password), st.session_state.campaigns_dict[campaign_name], rol)
    
        
render()