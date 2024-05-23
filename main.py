import streamlit as st
import mysql.connector
import pandas as pd
import numpy as np
import pytz

def separar_numero(numero):
    if len(numero) != 10 or not numero.isdigit():
        return "El número telefónico debe contener exactamente 10 dígitos."

    if numero.startswith("55"):
        return "-".join([numero[:2], numero[2:6], numero[6:]])
    else:
        return "-".join([numero[:3], numero[3:6], numero[6:8], numero[8:]])

num2curr = lambda x: "${:,.2f}".format(float(x))

st.set_page_config(page_title="CRM", page_icon="./img/logo_pernexium.png", layout="wide")

# Zona horaria de la Ciudad de México
zona_horaria= pytz.timezone('America/Mexico_City')

AGENTES = {
    "test@example.com":"Carlos Alberto García García",
    "test@test.com":"Carlos Alberto García García",
    "enrique.ramirez@pernexium.com": "Enrique Ramírez"
}
NOMBRE = AGENTES[st.experimental_user["email"]]

with st.sidebar:
    #st.image("./img/logo_pernexium.png", width =100)
    page = st.selectbox(
    'Selecciona la página',
    ('Inicio',
    'Sesión',
    'Re-intento contacto'))
        
if page == 'Inicio':        
    st.header(f"¡Hola, {NOMBRE.split(' ')[0]}!")
    
if page == 'Sesión':        
    
    st.header(f"Jairo Enrique Ramírez Sánchez")
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(f"**Producto**: {'TDC_Oro_visa'}")    
    with col2:
        st.write(f"**Saldo vencido:** {num2curr(10_000)}")
    with col3:
        st.write(f"**Teléfono:** {separar_numero('7151136840')}")
    
    # AGREGANDO ÚLTIMO PAGO E INTERACCIONES AL SIDE BAR
    
    with st.sidebar:
        st.write(f"**Último pago:** 30/04/2024")
        
        # Crear datos de ejemplo
        fechas = pd.date_range(start='2024-04-01', end='2024-04-30', freq='W')
        dictaminacion = np.random.choice(["PAGO PARCIAL", "PROMESA DE PAGO", "CLIENTE NO DEFINE", "SEGUIMIENTO A PP", "PAGO EFECTUADO"], size=len(fechas))

        # Crear DataFrame
        df = pd.DataFrame({
            'fecha': fechas,
            'dictaminación': dictaminacion
        })
        
        df = df.sort_values(by = 'fecha', ascending=False)
        
        st.write(f"**Historial de contacto:**")
        st.dataframe(df)
    
    st.divider()
    
    st.subheader("Demográficos")
    
    col1, col2, col3 = st.columns([1,1,2])
    with col1:
        st.write(f"**Edad**: {22}")    
    with col2:
        st.write(f"**Estado** {'Michoacán'}")
    with col3:
        st.write(f"**Correo:** {'enrique.ramirez@pernexium.com'}")
        
    st.divider()
    
    st.subheader("Dictaminación")
    
    arbol_dictaminacion = {
    "CONTACTO": [
        "PAGO PARCIAL",
        "PROMESA DE PAGO",
        "CLIENTE NO DEFINE",
        "SEGUIMIENTO A PP",
        "PAGO EFECTUADO",
        "CUENTA LIQUIDADA",
        "MENSAJE CON TERCEROS",
        "MENSAJE CON FAMILIAR",
        "DEFUNCION",
        "ACLARACION",
        "CUENTA CORRIENTE",
        "NEGATIVA DE PAGO",
        "LLAMAR DESPUES"
    ],
    "NO CONTACTO": [
        "BUZON DE VOZ",
        "ILOCALIZABLE",
        "NO CONTESTA",
        "CUELGA LLAMADA",
        "FUERA DE SERVICIO",
        "TELEFONO EQUIVOCADO"
    ]
    }
    
    col1, col2, col3 = st.columns(3)
    with col1:
        dictamen = st.selectbox(
        'Selecciona el dictamen',
            arbol_dictaminacion.keys()
        )
    with col2:
        subdictamen = st.selectbox(
        'Selecciona el subdictamen',
            arbol_dictaminacion[dictamen]
        )
        
    with col3:
        if subdictamen == "PROMESA DE PAGO":
            promesa_fecha = st.date_input("Fecha promesa")
            promesa_cantidad = st.number_input("Cantidad promesa")
            
        
    comentarios = st.text_area(
                "Comentarios","")
    
    
    st.button("Guardar")
    
    
