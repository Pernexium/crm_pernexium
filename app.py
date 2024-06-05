import streamlit as st
import pytz
from page_config import switch_page
from components.button import Button

st.set_page_config(page_title="CRM", page_icon="./img/logo_pernexium.png", layout="wide")

def render():

    if st.session_state.get('logged_in'):
        switch_page('home')

    if st.session_state.get('redirected_to_login'):
        st.toast("Debes iniciar sesión para acceder a esta página.")
        st.session_state['redirected_to_login'] = False
    
    st.header("Base App")

    if Button(None, "Login", None, "primary"):
        login()

def login():
    st.session_state['logged_in'] = dict(
        agent_id = "1",
        agent_name = "Juan Pérez",
        agent_role = "Administrador"
    )
    switch_page('home')


render()