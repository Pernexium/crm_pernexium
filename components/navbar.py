import streamlit as st


def Navbar(labels, callbacks, parent = st, border = True):
    with parent.container(border = border):    
        cols = parent.columns(len(labels))

        for col, label, callback in zip(cols, labels, callbacks):
            with col:
                if parent.button(label):
                    callback()
