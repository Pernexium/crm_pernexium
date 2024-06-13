import streamlit as st
from components.fields import DataField, SelectField, TextArea, DateField, NumberField
from components.button import Button
from components.br import BR
from utils import session_state, insert_interaction_result, get_credit_interactions, get_contact_status, get_corr_contact_substatus, get_id_from_name
from datetime import datetime


def RegistroDictaminacion(id, credito, parent = st, border = True):


    get_contact_status()

    with parent.container(border = border):
        parent.subheader("Dictaminación")

        col1, col2  = parent.columns(2)

        with col1:
            dictamen = SelectField(f"dictamen_{id}", "Selecciona el Dictamen", st.session_state.contact_status.name,  parent)
        with col2: 
            subdictamen = SelectField(f"subdictamen_{id}", "Selecciona el Subdictamen",  get_corr_contact_substatus(dictamen).name, parent)

        if subdictamen == "Promesa de Pago":
            with parent.container(border = True):
                parent.write("**Promesa de Pago**")
                BR(1, parent)
                promesa_fecha = DateField(f"promesa_fecha_{id}", "Fecha promesa", parent = parent, border = False)
                promesa_cantidad = NumberField(f"promesa_cantidad_{id}", "Cantidad promesa", parent = parent, border = False)

        comentarios = TextArea(f"comentarios_{id}", "Comentarios", "", parent)

        Button(f"guardar_dictaminacion_{id}", "Guardar", lambda: handle_guardar(id, credito), "primary", parent)

        BR(2, parent)


def handle_guardar(id, credito):
    
    subdictamen = session_state(f'subdictamen_{id}')
    promesa_de_pago = subdictamen == "Promesa de Pago"

    data = dict(
        assignment_id= credito["assignment_id"],
        contact_status_id= get_id_from_name(session_state(f'dictamen_{id}'), st.session_state.contact_status).contact_status_id,
        contact_substatus_id= get_id_from_name(subdictamen, st.session_state.sub_contact_status).contact_status_id,
        comments= session_state(f'comentarios_{id}') or 'NULL',
        payment_promise_date= session_state(f'promesa_fecha_{id}') if promesa_de_pago else 'NULL',
        payment_promise_amount= session_state(f'promesa_cantidad_{id}') if promesa_de_pago else 'NULL',
    )

    print(data)

    insert_interaction_result(**data)

    print(f"Guardado: {', '.join([f'{k}: {v}' for k, v in data.items()])}")
    st.toast("Guardado correctamente")

    # Si ya obtuvimos los assignments
    if st.session_state.get('assignments') is not None:
        # Si ya obtuvimos las interacciones de este crédito
        if st.session_state.assignments.interactions.get(credito['credit_id']) is not None:
            # Reobtenemos las interacciones
            st.session_state.assignments.interactions[credito['credit_id']] = None
            get_credit_interactions(credito['credit_id'])
