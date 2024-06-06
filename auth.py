import streamlit as st
import hashlib
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from utils import use_sql_client

@use_sql_client
def insert_user(name, email, password, campaign_name, rol):
    success = False
    try:
        st.session_state.sql_client.insert_user(name, email, hash_password(email, password), campaign_name, rol)
        st.toast("Usuario registrado con éxito")
        success = True
    except IntegrityError as e:
        st.toast("Error al insertar el usuario: El correo ya existe.")
    except SQLAlchemyError as e:
        st.toast(f"Error al insertar el usuario: {e}")
    finally:
        return success
            
            
def hash_password(email, password):
    pass_bytes = f"{email}{password}".encode('utf-8')
    password_hash = hashlib.sha256(pass_bytes).hexdigest()
    return password_hash

@use_sql_client
def login_email_lookup(email):
    return st.session_state.sql_client.login_email_lookup(email)


def try_login(email, password):
    user = login_email_lookup(email)
    if user is None:
        st.error("Correo no registrado.")
        st.session_state['logged_in'] = False
        return
    
    user["user_id"] = 1

    if user["pass"] != hash_password(email, password):
        st.error("Contraseña incorrecta.")
        st.session_state['logged_in'] = False
        return
    
    st.session_state['logged_in'] = user