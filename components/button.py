import streamlit as st

def Button(label, callback, type = "primary", parent = st):
    return parent.button(label, on_click=callback, type = type)