import streamlit as st
from containers.registro_dictaminacion import RegistroDictaminacion
from components.fields import TextField, SelectField
from components.button import Button
from components.table import Table
from components.br import BR
from page_config import inject_navbar, inject_table_css, require_login
from utils import session_state, get_dummy_table
from const import SCHEMAS
import pandas as pd

st.set_page_config(page_title="CRM - Búsqueda", page_icon="./img/logo_pernexium.png", layout="wide")

@inject_navbar
@inject_table_css
@require_login
def render(parent = st):

    with parent.container(border = True):
        parent.header("Busqueda")

        with parent.container(border = True):
            id, nombre, telefono, buscar = parent.columns(4, gap = "large")

            with id:
                TextField("buscar_id", "ID", "", parent, border = False)
            with nombre:
                TextField("buscar_nombre", "Nombre", "", parent, border = False)
            with telefono:
                TextField("buscar_telefono", "Teléfono", "", parent, border = False)
            with buscar:
                Button("buscar_contacto", "Buscar", handle_buscar , "primary", parent)

        BR(2, parent)

        buscar_tabla = session_state('buscar_tabla')
        if buscar_tabla is not None:
            Table(buscar_tabla, parent)
            BR(2, parent)
            
            col1, _ = parent.columns([1, 1])
            with col1:
                id_seleccionado = SelectField("buscar_id_tabla", "Selecciona un contacto", ["1", "2", "3"], parent, border = False)

            BR(2, parent)

            RegistroDictaminacion("busqueda", parent)


def handle_buscar():

    data = dict(
        id = session_state('buscar_id'),
        nombre = session_state('buscar_nombre'),
        telefono = session_state('buscar_telefono'),
    )

    if all(map(lambda x: not x, data.values())): 
        st.error("Debes ingresar al menos un campo para buscar")
        return


    print(f"BUSCANDO: {', '.join([f'{k}: {v}' for k, v in data.items()])}")

    #

    st.session_state['buscar_tabla'] = get_dummy_table("credito")


render()