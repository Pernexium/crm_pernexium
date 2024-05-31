import streamlit as st

def DescargaManual():
    st.header("Descarga Manual")

    st.write("En esta sección podrás descargar la información de tus clientes en formato xlsx en caso de que el sistema haya fallado en la asignación automática")

    st.write("Da click en descargar . . .")

    st.button("Descargar", on_click=download_manual, type = "primary")


def download_manual():
    st.toast("Descarga exitosa")