import streamlit as st
from containers.registro_dictaminacion import RegistroDictaminacion
from components.fields import TextField, SelectField
from components.button import Button
from components.table import Table
from components.br import BR
from page_config import inject_navbar, inject_stylesheet, require_login
from utils import session_state, search_credit
from const import SCHEMAS
import pandas as pd

st.set_page_config(page_title="CRM - Búsqueda", page_icon="./img/logo_pernexium.png", layout="wide")

@require_login
@inject_stylesheet
@inject_navbar
def render(parent = st):

    with parent.container(border = True):
        parent.header("Busqueda")

        with parent.container(border = True):
            id, nombre, telefono, buscar = parent.columns(4, gap = "large")

            with id:
                TextField("buscar_credit_id", "ID Crédito", "", parent, border = False)
            with nombre:
                TextField("buscar_name", "Nombre", "", parent, border = False)
            with telefono:
                TextField("buscar_phone_number", "Teléfono", "", parent, border = False)
            with buscar:
                Button("buscar_contacto", "Buscar", handle_buscar , "primary", parent)

        BR(2, parent)

        buscar_tabla = st.session_state.get("busqueda_tabla", None)
        if buscar_tabla is not None and not buscar_tabla.empty:
            Table(buscar_tabla, parent)
            BR(2, parent)
            
            col1, _ = parent.columns([1, 1])
            with col1:
                id_seleccionado = SelectField("buscar_id_tabla", "Selecciona un crédito", buscar_tabla['credit_id'], parent, border = False)
            
            credito_seleccionado = buscar_tabla[buscar_tabla['credit_id'] == id_seleccionado].iloc[0].to_dict()

            BR(2, parent)

            RegistroDictaminacion("busqueda", credito_seleccionado, parent)


def handle_buscar():

    data = dict(
        credit_id = session_state('buscar_credit_id'),
        name = session_state('buscar_name'),
        phone_number = session_state('buscar_phone_number'),
    )

    if all(map(lambda x: not x, data.values())): 
        st.error("Debes ingresar almenos un campo para buscar")
        return


    print(f"BUSCANDO: {', '.join([f'{k}: {v}' for k, v in data.items()])}")

    search_credit(**data)

render()