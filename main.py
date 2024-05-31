import streamlit as st
import pytz
from utils import *
from const import ARBOL_DICTAMINACION, AGENTES

from page.home import Home
from page.sesion import Sesion
from page.busqueda import Busqueda
from page.dashboard import Dashboard
from page.descarga_manual import DescargaManual

from components.navbar import Navbar

st.set_page_config(page_title="CRM", page_icon="./img/logo_pernexium.png", layout="wide")

st.session_state['nombre'] = AGENTES[st.experimental_user["email"]]
# Zona horaria de la Ciudad de México    
st.session_state['zona_horaria'] = pytz.timezone('America/Mexico_City')


if __name__ == "__main__":

    inicio, sesion, busqueda, dashboard, descarga_manual = st.tabs(["Inicio", "Sesión", "Búsqueda", "Dashboard", "Descarga Manual"])

    with inicio:
        Home()
    with sesion:
        Sesion()
    with busqueda:
        Busqueda()
    with dashboard:
        Dashboard()
    with descarga_manual:
        DescargaManual()
