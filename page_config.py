import streamlit as st
from containers.navbar import Navbar
from components.button import Button
import pytz

def page_config(func):
    # Zona horaria de la Ciudad de México    
    if not st.session_state.get('zona_horaria'):
        st.session_state['zona_horaria'] = pytz.timezone('America/Mexico_City')
    return func


def switch_page(page):
    st.switch_page(f"./pages/{page}.py")

def inject_navbar(page):
    def wrapper():
        Navbar(
            ["Inicio", "Sesión", "Búsqueda", "Dashboard", "Descarga Manual", "Registro de Usuario"],
            [
                lambda: switch_page("home"), 
                lambda: switch_page("sesion"),
                lambda: switch_page("busqueda"),
                lambda: switch_page("dashboard"),
                lambda: switch_page("descarga_manual"),
                lambda: switch_page("registro_usuario"),
            ]
        )
        page()
    return wrapper

def require_login(page):
    def wrapper():
        if not st.session_state.get('logged_in') and st.secrets.auth.require_login:
            return_login(True)

        _, container = st.columns([5/6, 1/6])
        with container:
            if Button(None, "Logout", callback= None , parent = st):
                logout()
        
        page()
    return wrapper

def logout():
    if st.session_state.get("assignments"):
        del st.session_state["assignments"]
    return_login(False)

def return_login(failed_redirection = False):
    st.session_state['logged_in'] = False
    st.session_state['redirected_to_login'] = failed_redirection
    st.switch_page("./app.py")

def inject_stylesheet(page):
    def wrapper():
        if st.session_state.get('css_classes') is None:
            with open('./css/stylesheet.html', 'r') as f:
                st.session_state.css_classes = f.read()
        st.write(st.session_state.css_classes, unsafe_allow_html=True)
        page()
    return wrapper