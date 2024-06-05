import streamlit as st
import numpy as np
import pandas as pd
from const import ARBOL_DICTAMINACION
from components.table import Table
from components.fields import DataField
from components.br import BR
from components.button import Button
from containers.registro_dictaminacion import RegistroDictaminacion
from utils import *
from page_config import inject_navbar, inject_table_css, require_login

st.set_page_config(page_title="CRM - Sesión", page_icon="./img/logo_pernexium.png", layout="wide")


@inject_navbar
@inject_table_css
@require_login
def render(parent = st):

    fetch_assignments()

    BR(3, parent)
    
    SesionNav()
    
    with parent.container(border = True):

        parent.header("Nombre del Cliente")

        BR(3, parent)

        col1, col2  = parent.columns(2, gap = "large")

        with col1: 
            DataField("ID", "", parent)
            DataField("Teléfono", "", parent)
            DataField("Correo", "", parent)
        with col2: 
            DataField("Producto", "", parent)
            DataField("Saldo Vencido Actual", "", parent)
            DataField("Saldo a Liquidar", "", parent)

        BR(2, parent)

    with parent.container(border = True):
        tablas, registro = parent.tabs(["Tablas", "Registro"])

        with tablas:
            contacto, pagos, chatbot = parent.tabs (["Contacto", "Pagos", "Chatbot"])

            with contacto:
                Table(get_dummy_table("dictaminacion"), parent)

            with pagos:
                Table(get_dummy_table("pagos"), parent)

            with chatbot:
                Table(get_dummy_table("chatbot"), parent)

            BR(2, parent)

        with registro:
            RegistroDictaminacion("sesion", {}, parent, border = False)


def SesionNav(parent = st):
    _, container = parent.columns([4/5, 1/5])
    with container:
        with parent.container(border = False):
            anterior, siguiente = parent.columns(2)
            with anterior:
                Button("session_previous", "Anterior", callback= session_previous , parent = parent)
            with siguiente:
                Button("session_next", "Siguiente", callback= session_next, parent = parent)

def session_previous():
    print("previous")

def session_next():
    print("next")



render()