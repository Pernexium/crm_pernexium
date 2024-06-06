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
from page_config import inject_navbar, inject_stylesheet, require_login

st.set_page_config(page_title="CRM - Sesión", page_icon="./img/logo_pernexium.png", layout="wide")


@require_login
@inject_stylesheet
@inject_navbar
def render(parent = st):

    fetch_assignments()

    assignments = st.session_state.assignments
    if assignments.assignments.empty:
        parent.error("No hay asignaciones disponibles")
        return
    
    current_assignment = assignments.assignments.iloc[assignments.current_assignment].to_dict()
    credit_id = current_assignment["credit_id"]

    get_all_session_tables(credit_id)

    interactions = assignments.interactions[credit_id]
    payments = assignments.payments[credit_id]
    chatbot_interactions = assignments.chatbot[credit_id]


    BR(3, parent)
    
    SesionNav()
    
    with parent.container(border = True):

        parent.header(current_assignment["name"])

        BR(3, parent)

        col1, col2  = parent.columns(2, gap = "large")

        with col1: 
            DataField("ID", current_assignment["client_id"], parent)
            DataField("Teléfono", current_assignment["phone_number"], parent)
            DataField("Correo", current_assignment["email"], parent)
        with col2: 
            DataField("Producto", current_assignment["product"], parent)
            DataField("Saldo Vencido Actual", current_assignment["current_balance"], parent)
            DataField("Saldo a Liquidar", current_assignment["balance_to_settle"], parent)

        BR(2, parent)

    with parent.container(border = True):
        tablas, registro = parent.tabs(["Tablas", "Registro"])

        with tablas:
            contacto, pagos, chatbot = parent.tabs(["Contacto", "Pagos", "Chatbot"])

            with contacto:
                Table(interactions, parent)

            with pagos:
                Table(payments, parent)

            with chatbot:
                Table(chatbot_interactions, parent)

            BR(2, parent)

        with registro:
            RegistroDictaminacion("sesion", current_assignment, parent, border = False)


def SesionNav(parent = st):
    _, container = parent.columns([4/5, 1/5])
    with container:
        with parent.container(border = False):
            anterior, siguiente = parent.columns(2)
            with anterior:
                if st.session_state.assignments.current_assignment > 0:
                    Button("session_previous", "Anterior", callback= session_previous , parent = parent)
            with siguiente:
                if st.session_state.assignments.current_assignment < st.session_state.assignments.n_assignments - 1:
                    Button("session_next", "Siguiente", callback= session_next, parent = parent)

def session_previous():
    st.session_state.assignments.current_assignment = max(0 , st.session_state.assignments.current_assignment - 1)

def session_next():
    st.session_state.assignments.current_assignment = min(st.session_state.assignments.n_assignments - 1, st.session_state.assignments.current_assignment + 1)



render()