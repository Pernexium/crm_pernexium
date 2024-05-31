import streamlit as st

def Button(key, label, callback, type = "primary", parent = st):
    return parent.button(label, key = key, on_click=callback, type = type)