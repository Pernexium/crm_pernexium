import streamlit as st
import plotly.graph_objects as go
from const import DIAS, BAR_HEIGHT, COLORS, MESES
from components.kpi import KPI
from components.br import BR
from components.fields import SelectField
from page_config import inject_navbar, inject_table_css, require_login

st.set_page_config(page_title="CRM - Dashboard", page_icon="./img/logo_pernexium.png", layout="wide")


@inject_table_css
@inject_navbar
@require_login
def render(parent = st):
    parent.header("Dashboard")

    _, kpi_container, _ = parent.columns([1/4, 1/2, 1/4])
    with kpi_container:
        kp1, kpi2 = parent.columns(2)
        
        with kp1:
            KPI("Eficiencia", "0.675",  parent= parent)
        with kpi2:
            KPI("Total Promesas", "$3,532.325", parent = parent)

    BR(2, parent)


    _, mes_field = parent.columns([2/3, 1/3])

    with mes_field:
        mes = SelectField("mes", "Selecciona un mes", MESES, parent, border = False)

    with parent.container(border = False):
        # Create the bar plot
        fig = go.Figure(data=[go.Bar(x=DIAS, y=BAR_HEIGHT, marker_color = COLORS['secondary'])])
        # Update the layout for titles
        fig.update_layout(
            title={
                'text': f'Suma de créditos pagados gestionados por el agente en {mes}',
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top',
            },
            xaxis_title='Días del mes',
            yaxis_title='Suma de Créditos Pagados'
        )

        parent.plotly_chart(fig)

render()