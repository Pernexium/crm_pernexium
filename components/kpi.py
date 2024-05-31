import streamlit as st
from const import COLORS

def KPI(label, value, type = "primary", parent = st):
    with parent.container(border = True):
        parent.write(
            f"""
            <div class="centered kpi">
                <p style="color: {COLORS[type]}">{value}</p>
                <p>{label}</p>
            </div>
            """,
        unsafe_allow_html=True)