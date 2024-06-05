import streamlit as st
from components.fields import DataField, SelectField, TextArea, DateField, NumberField
from const import ARBOL_DICTAMINACION
from components.button import Button
from components.br import BR
from utils import session_state


## Tiene que recibir el id porque se está renderizando más de una vez a pesar de no ser mostrado en pantalla
## Esto sucede proque tabs renderiza todos los contenedores al mismo tiempo, en vez de únicamente lo contenido en la
## tab activa

def RegistroDictaminacion(id, credito, parent = st, border = True):

    with parent.container(border = border):
        parent.subheader("Dictaminación")

        col1, col2  = parent.columns(2)

        with col1:
            dictamen = SelectField(f"dictamen_{id}", "Selecciona el Dictamen", ARBOL_DICTAMINACION.keys(),  parent)
        with col2: 
            subdictamen = SelectField(f"subdictamen_{id}", "Selecciona el Subdictamen", ARBOL_DICTAMINACION[dictamen], parent)

        if subdictamen == "PROMESA DE PAGO":
            with parent.container(border = True):
                parent.write("**Promesa de Pago**")
                BR(1, parent)
                promesa_fecha = DateField(f"promesa_fecha_{id}", "Fecha promesa", parent = parent, border = False)
                promesa_cantidad = NumberField(f"promesa_cantidad_{id}", "Cantidad promesa", parent = parent, border = False)

        comentarios = TextArea(f"comentarios_{id}", "Comentarios", "", parent)

        Button(f"guardar_dictaminacion_{id}", "Guardar", lambda: handle_guardar(id), "primary", parent)

        BR(2, parent)


def handle_guardar(id):
    
    subdictamen = session_state(f'subdictamen_{id}')
    data = dict(
        dictamen = session_state(f'dictamen_{id}'),
        subdictamen = subdictamen,
        comentarios = session_state(f'comentarios_{id}'),
        fecha_promesa = session_state(f'promesa_fecha_{id}') if subdictamen == "PROMESA DE PAGO" else None,
        cantidad_promesa = session_state(f'promesa_cantidad_{id}') if subdictamen == "PROMESA DE PAGO" else None,
    )

    print(f"Guardado: {', '.join([f'{k}: {v}' for k, v in data.items()])}")
    st.toast("Guardado correctamente")
