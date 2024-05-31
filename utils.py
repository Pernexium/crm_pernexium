import streamlit as st
from const import SCHEMAS
import pandas as pd

def separar_numero(numero):
    if len(numero) != 10 or not numero.isdigit():
        return "El número telefónico debe contener exactamente 10 dígitos."

    if numero.startswith("55"):
        return "-".join([numero[:2], numero[2:6], numero[6:]])
    else:
        return "-".join([numero[:3], numero[3:6], numero[6:8], numero[8:]])

def num2curr(x): 
    return "${:,.2f}".format(float(x))

def session_state(key):
    return st.session_state.get(key)

def get_dummy_table(key):
    table_columns = [{k: '' for k in SCHEMAS[key].values()}]
    return pd.DataFrame(table_columns)