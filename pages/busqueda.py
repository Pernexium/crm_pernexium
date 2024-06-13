import streamlit as st
from containers.registro_dictaminacion import RegistroDictaminacion
from components.fields import TextField, SelectField
from components.button import Button
from components.table import Table
from components.br import BR
from page_config import inject_navbar, inject_stylesheet, require_login
from utils import session_state, search_credit
import pandas as pd

st.set_page_config(page_title="CRM - Búsqueda", page_icon="./img/logo_pernexium.png", layout="wide")

@require_login
@inject_stylesheet
@inject_navbar
def render(parent = st):

    with parent.container(border = True):
        parent.header("Busqueda")

        with parent.container(border = True):
            valor, buscar = parent.columns(2, gap = "large")
            with valor:
                TextField("buscar_valor", "ID, teléfono o nombre", "", parent, border = False)
            
            with buscar:
                Button("buscar_contacto", "Buscar", handle_buscar , "primary", parent)
            

        BR(2, parent)

        buscar_tabla = st.session_state.get("busqueda_tabla", None)
        if buscar_tabla is not None and not buscar_tabla.empty:
            Table(buscar_tabla, parent)
            BR(2, parent)
            
            col1, _ = parent.columns([1, 1])
            with col1:
                id_seleccionado = SelectField("buscar_id_tabla", "Selecciona un crédito", buscar_tabla.index, parent, border = False)
            
            credito_seleccionado = buscar_tabla.loc[id_seleccionado]

            BR(2, parent)

            RegistroDictaminacion("busqueda", credito_seleccionado, parent)


def handle_buscar():

    data = dict(
        value = session_state('buscar_valor')
    )

    if all(map(lambda x: not x, data.values())): 
        st.error("Debes ingresar almenos un campo para buscar")
        return


    print(f"BUSCANDO: {', '.join([f'{k}: {v}' for k, v in data.items()])}")

    search_credit(**data)

render()