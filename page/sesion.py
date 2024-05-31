import streamlit as st
import numpy as np
import pandas as pd
from const import ARBOL_DICTAMINACION, AGENTES, SCHEMAS
from components.table import Table
from components.fields import DataField, SelectField, TextArea, DateField, NumberField
from components.br import BR
from components.button import Button
from utils import *

def Sesion(parent = st):
    
    with parent.container(border = True):

        parent.header("Nombre del Cliente")

        BR(3, parent)

        col1, col2  = parent.columns(2, gap = "large")

        with col1: 
            DataField("ID", "1-23jkl", parent)
            DataField("Teléfono", "23094823", parent)
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
                table_columns = [{k: '' for k in SCHEMAS["dictaminacion"].values()}]
                Table(pd.DataFrame(table_columns), parent)

            with pagos:
                table_columns = [{k: '' for k in SCHEMAS["pagos"].values()}]
                Table(pd.DataFrame(table_columns), parent)

            with chatbot:
                table_columns = [{k: '' for k in SCHEMAS["chatbot"].values()}]
                Table(pd.DataFrame(table_columns), parent)

        with registro:

            parent.subheader("Dictaminación")

            col1, col2  = parent.columns(2)

            with col1:
                dictamen = SelectField("dictamen", "Selecciona el Dictamen", ARBOL_DICTAMINACION.keys(),  parent)
            with col2: 
                subdictamen = SelectField("subdictamen", "Selecciona el Subdictamen", ARBOL_DICTAMINACION[dictamen], parent)

            if subdictamen == "PROMESA DE PAGO":
                with parent.container(border = True):
                    parent.write("**Promesa de Pago**")
                    BR(1, parent)
                    promesa_fecha = DateField("promesa_fecha", "Fecha promesa", parent = parent, border = False)
                    promesa_cantidad = NumberField("promesa_cantidad", "Cantidad promesa", parent = parent, border = False)

            comentarios = TextArea("comentarios", "Comentarios", "", parent)

            Button("Guardar", lambda: handle_guardar(), "primary", parent)

            BR(2, parent)


def handle_guardar():
    
    subdictamen = session_state('subdictamen'),
    data = dict(
        dictamen = session_state('dictamen'),
        subdictamen = subdictamen,
        comentarios = session_state('comentarios'),
        fecha_promesa = session_state('promesa_fecha') if subdictamen == "PROMESA DE PAGO" else None,
        cantidad_promesa = session_state('promesa_cantidad') if subdictamen == "PROMESA DE PAGO" else None,
    )

    print(f"Guardado: {', '.join([f'{k}: {v}' for k, v in data.items()])}")
    st.toast("Guardado correctamente")
