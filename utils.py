import streamlit as st
from const import SCHEMAS
import pandas as pd
from cliente_sql import SqlClient
from sqlalchemy.exc import SQLAlchemyError
from functools import wraps
from dataclasses import dataclass


@dataclass
class Assignments:
    assignments: pd.DataFrame
    current_assignment: int
    n_assignments: int

    interactions: dict
    payments: dict
    chatbot: dict


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


def use_sql_client(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not session_state('sql_client'):
            if not st.secrets.get('db_credentials'):
                st.error("No se encontraron las credenciales de la base de datos.")
                st.stop()

            st.session_state['sql_client'] = SqlClient(**st.secrets.db_credentials)

        try: 
            return func(*args, **kwargs)
        except SQLAlchemyError as e:
            print(e)
            st.error("Ocurrió un error en la base de datos.")
            st.stop()
    return wrapper


@use_sql_client
def fetch_assignments():
    if st.session_state.get('assignments') is None:
        print(f"FECTCHING ASSIGNMENTS PARA USUARIO: {user_data('agent_name'), user_data('user_id')}")
        assigmnents = st.session_state.sql_client.get_agent_assignments(user_data('user_id'))
        st.session_state['assignments'] = Assignments(
            assignments= assigmnents,
            current_assignment = 0,
            n_assignments= len(assigmnents),
            interactions = {k: None for k in assigmnents['credit_id']},
            payments = {k: None for k in assigmnents['credit_id']},
            chatbot = {k: None for k in assigmnents['credit_id']}
        )



@use_sql_client
def get_credit_interactions(credit_id):
    if st.session_state.assignments.interactions[credit_id] is None:
        print(f"FETCHING CREDIT INTERACTIONS: {credit_id}")
        interactions = st.session_state.sql_client.get_interaction_results(credit_id).set_index('opinion_id')
        st.session_state.assignments.interactions[credit_id] = interactions


@use_sql_client
def get_credit_payments(credit_id):
    if st.session_state.assignments.payments[credit_id] is None:
        print(f"FETCHING CREDIT PAYMENTS: {credit_id}")
        payments = st.session_state.sql_client.get_credit_payments(credit_id).set_index('payment_id')
        st.session_state.assignments.payments[credit_id] = payments

@use_sql_client
def get_credit_chatbot_interactions(credit_id):
    # # TODO: QUERY DEL CHATBOT
    # if st.session_state.assignments.chatbot[credit_id] is None:
    #     print(f"FETCHING CREDIT CHATBOT INTERACTIONS: {credit_id}")
    #     chatbot = st.session_state.sql_client.get_credit_chatbot_interactions(credit_id)
    #     st.session_state.assignments.chatbot[credit_id] = chatbot
    st.session_state.assignments.chatbot[credit_id] = None

def get_all_session_tables(credit_id):
    get_credit_interactions(credit_id)
    get_credit_payments(credit_id)
    get_credit_chatbot_interactions(credit_id)


@use_sql_client
def insert_interaction_result(assignment_id, contact_date, contact_status, contact_substatus, comments, payment_promise_date, payment_promise_amount):
    st.session_state.sql_client.insert_interaction_result(
        assignment_id = assignment_id,
        contact_date = contact_date,
        contact_status = contact_status,
        contact_substatus = contact_substatus,
        comments = comments,
        payment_promise_date = payment_promise_date,
        payment_promise_amount = payment_promise_amount
    )



@use_sql_client
def search_credit(valor):
    st.session_state["busqueda_tabla"] = st.session_state.sql_client.search_credit(valor)



@use_sql_client
def get_campaings_name():
    if st.session_state.get("campaigns") is None:
        print("FETCHING CAMPAIGNS")
        st.session_state["campaigns"] = st.session_state.sql_client.get_campaings_name()
