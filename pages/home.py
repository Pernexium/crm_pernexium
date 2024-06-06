import streamlit as st
from page_config import inject_navbar, require_login

st.set_page_config(page_title="CRM - Inicio", page_icon="./img/logo_pernexium.png", layout="wide")

@require_login
@inject_navbar
def render(parent = st):
    parent.header(f"Bienvenido {st.session_state['logged_in']['name']}")
    parent.write("Bienvenido al CRM de Pernexium. Aquí podrás encontrar toda la información de tus clientes y gestionar tus tareas de manera eficiente.")

render()