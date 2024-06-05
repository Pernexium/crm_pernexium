import streamlit as st
from components.fields import TextField, PasswordField
from components.br import BR
from components.button import Button
from page_config import inject_navbar, require_login

st.set_page_config(page_title="CRM - Registro Usuario", page_icon="./img/logo_pernexium.png", layout="wide")

@inject_navbar
@require_login
def render(parent = st):
    parent.header("Registro de Usuario")

    with parent.container(border = True):

        _, fieldset, _ = parent.columns([1, 6, 1])

        with fieldset:
            BR(2, parent)

            nombre = TextField("nombre_registro_usuario", "Nombre", "", parent, border = False)
  
            correo = TextField("correo_registro_usuario", "Correo", "", parent, border = False)

            password = PasswordField("password_registro_usuario", "Contraseña", "", parent, border = False)

            password_ver = PasswordField("password_ver_registro_usuario", "Verificar Contraseña", "", parent, border = False)

            BR(2, parent)
            
            Button("registrar_usuario", "Registrar", handle_registrar, "primary", parent)


def handle_registrar():
    print("REGISTRO DE DATOS")

    nombre = st.session_state.get("nombre_registro_usuario")
    correo = st.session_state.get("correo_registro_usuario")
    password = st.session_state.get("password_registro_usuario")
    password_ver = st.session_state.get("password_ver_registro_usuario")

    if not nombre or not correo or not password or not password_ver:
        st.error("Debes llenar todos los campos")
        return
    
    if password != password_ver:
        st.error("Las contraseñas no coinciden")
        return
    
    st.success("Usuario registrado con éxito")

        
render()