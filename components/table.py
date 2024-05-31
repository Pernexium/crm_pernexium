import streamlit as st
import pandas as pd


#TODO: si la busqueda encuentra 100000 registros se hará gigantesca, valorar con parent.table
def Table(data : pd.DataFrame | None = None, parent = st):
    # parent.table(data)
    if data is None:
        data = pd.DataFrame()
    data = data.set_index("Id").style.set_properties(**{'text-align': 'start'})
    parent.write(data.to_html(escape=False), unsafe_allow_html=True)