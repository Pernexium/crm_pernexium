import streamlit as st
from page_config import inject_navbar, inject_table_css, require_login

st.set_page_config(page_title="CRM - Inicio", page_icon="./img/logo_pernexium.png", layout="wide")

@inject_navbar
@require_login
def render(parent = st):
    parent.header("Bienvenido al CRM de Pernexium")
    parent.write("Bienvenido al CRM de Pernexium. Aquí podrás encontrar toda la información de tus clientes y gestionar tus tareas de manera eficiente.")
    parent.write("lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.")

render()