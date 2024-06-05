import streamlit as st
from components.button import Button

def Navbar(labels, callbacks, parent = st, border = True):
    with parent.container(border = border):    
        cols = parent.columns(len(labels))

        for col, label, callback in zip(cols, labels, callbacks):
            with col:
                if Button(None, label, None, "secondary", parent):
                    callback()
