import streamlit as st


def DataField(label, value, parent = st, border = True):
    with parent.container(border = border):
        col1, col2 = parent.columns([1,2])
        with col1: 
            parent.write(f"**{label}**")
        with col2: 
            parent.write(f"{value}")


def SelectField(key, label, options, parent = st, border = True): 
    with parent.container(border = border):
        col1, col2 = parent.columns([1,2])
        with col1: 
            parent.write(f"**{label}**")
        with col2: 
            value = parent.selectbox("empty", options, key = key, label_visibility="collapsed")
    return value


def TextArea(key, label, value, parent = st, border = True):
    with parent.container(border = border):
        parent.write(f"**{label}**")
        text = parent.text_area("empty", value, key = key, label_visibility="collapsed")
    return text

def DateField(key, label, value = "today", parent = st, border = True):
    with parent.container(border = border):
        col1, col2 = parent.columns([1,2])
        with col1:
            parent.write(f"**{label}**")
        with col2:
            date = parent.date_input("empty", value, key = key, label_visibility="collapsed")
    return date

def NumberField(key, label, value = 0, parent = st, border = True):
    with parent.container(border = border):
        col1, col2 = parent.columns([1,2])
        with col1:
            parent.write(f"**{label}**")
        with col2:
            number = parent.number_input("empty", value = value, key = key, label_visibility="collapsed")
    return number
