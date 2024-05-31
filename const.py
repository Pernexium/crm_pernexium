ARBOL_DICTAMINACION = {
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


AGENTES = {
    "test@example.com":"Carlos Alberto García García",
    "test@test.com":"Carlos Alberto García García",
    "enrique.ramirez@pernexium.com": "Enrique Ramírez"
}

SCHEMAS = {
    "dictaminacion": {
        "id": "Id",
        "fecha_contacto": "Fecha de contacto",
        "estatus_dictaminacion": "Estatus de dictaminación",
        "estatus_contacto" : "Estatus de contacto",
        "comentarios": "Comentarios"
    },
    "pagos":{
        "id": "Id",
        "pago": "Pago",
        "fecha": "Fecha"
    },
    "chatbot": {
        "id": "Id",
        "fecha": "Fecha",
        "mensaje": "Mensaje",
        "usuario": "Usuario"
    }
}