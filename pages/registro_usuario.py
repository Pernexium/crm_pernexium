import streamlit as st
from components.fields import TextField, PasswordField, SelectField
from components.br import BR
from components.button import Button
from page_config import inject_navbar, require_login
from utils import get_campaings, get_roles, get_id_from_name
from auth import hash_password, insert_user


st.set_page_config(page_title="CRM - Registro Usuario", page_icon="./img/logo_pernexium.png", layout="wide")


@require_login
@inject_navbar
def render(parent = st):

    get_campaings()
    get_roles()

    campaigns = st.session_state.campaigns.name.to_list()
    roles = st.session_state.roles.name.to_list()
        
    parent.header("Registro de Usuario")

    with parent.container(border = True):

        _, fieldset, _ = parent.columns([1, 6, 1])

        with fieldset:
            BR(2, parent)

            nombre = TextField("nombre_registro_usuario", "Nombre", "", parent, border = False)
  
            correo = TextField("correo_registro_usuario", "Correo", "", parent, border = False)
    
            campania = SelectField("select_campaign", "Campaña", campaigns, parent = st, border = False)

            password = PasswordField("password_registro_usuario", "Contraseña", "", parent, border = False)

            password_ver = PasswordField("password_ver_registro_usuario", "Verificar Contraseña", "", parent, border = False)

            rol = SelectField("select_rol", "Rol", roles, parent = st, border = False)

            BR(2, parent)
            
            Button("registrar_usuario", "Registrar", handle_registrar, "primary", parent)

            
def handle_registrar():
    print("REGISTRO DE DATOS")

    nombre = st.session_state.get("nombre_registro_usuario")
    correo = st.session_state.get("correo_registro_usuario")
    password = st.session_state.get("password_registro_usuario")
    campaign_id = get_id_from_name(st.session_state.get("select_campaign"), st.session_state.campaigns).campaign_id
    password_ver = st.session_state.get("password_ver_registro_usuario")
    role_id = get_id_from_name(st.session_state.get("select_rol"), st.session_state.roles).role_id

    if not nombre or not correo or not password or not password_ver:
        st.error("Debes llenar todos los campos")
        return
    
    if password != password_ver:
        st.error("Las contraseñas no coinciden")
        return
    
    if insert_user(nombre, correo, password, campaign_id, role_id):
        # Clear fields
        st.session_state.nombre_registro_usuario = None
        st.session_state.correo_registro_usuario = None
        st.session_state.password_registro_usuario = None
        st.session_state.password_ver_registro_usuario = None
        st.session_state.select_campaign = None
        st.session_state.select_rol = None
        
        
render()