import streamlit as st
from page_config import inject_navbar, require_login

st.set_page_config(page_title="CRM - Descarga Manual", page_icon="./img/logo_pernexium.png", layout="wide")

@inject_navbar
@require_login
def render():
    st.header("Descarga Manual")

    st.write("En esta sección podrás descargar la información de tus clientes en formato xlsx en caso de que el sistema haya fallado en la asignación automática")

    st.write("Da click en descargar . . .")

    st.button("Descargar", on_click=download_manual, type = "primary")


def download_manual():
    st.toast("Descarga exitosa")

render()