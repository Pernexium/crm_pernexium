import streamlit as st
from const import SCHEMAS
import pandas as pd
from cliente_sql import SqlClient
import hashlib
from sqlalchemy import create_engine

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

def user_data(key):
    return st.session_state.get('logged_in').get(key)

def get_dummy_table(key):
    table_columns = [{k: '' for k in SCHEMAS[key].values()}]
    return pd.DataFrame(table_columns)


def use_sql_client(func):
    if not session_state('sql_client'):
        if not st.secrets.db_credentials:
            st.error("No se encontraron las credenciales de la base de datos.")
        st.session_state['sql_client'] = SqlClient(**st.secrets.db_credentials)

    return func

def hash_password(password):
    
    password_bytes = password.encode('utf-8')
    
    sha256 = hashlib.sha256()
    
    sha256.update(password_bytes)
    
    password_hash = sha256.hexdigest()
    return password_hash

def get_engine():
    host = st.secrets["db_credentials"]["host"]
    database = st.secrets["db_credentials"]["database"]
    user = st.secrets["db_credentials"]["user"]
    password = st.secrets["db_credentials"]["password"]

    # Crear la URL de la base de datos
    DATABASE_URL = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"

    # Crear el motor de SQLAlchemy
    return create_engine(DATABASE_URL)

@use_sql_client
def fetch_assignments():
    print(f"ASSIGNMENTS PARA USUARIO: {user_data('agent_name'), user_data('agent_id')}")