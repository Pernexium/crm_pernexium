import streamlit as st
import pandas as pd

def Table(data : pd.DataFrame | None = None, parent = st):
    parent.table(data)