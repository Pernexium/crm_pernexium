import streamlit as st



def Home(parent = st):       
    parent.header(f"¡Hola, {st.session_state.get('nombre').split(' ')[0]}!")

    parent.write("Bienvenido al CRM de Pernexium. Aquí podrás encontrar toda la información de tus clientes y gestionar tus tareas de manera eficiente.")
    parent.write("lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.")