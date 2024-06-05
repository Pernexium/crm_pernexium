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
    },
    "credito":{
        "id": "Id",
        "nombre": "Nombre Cliente",
        "telefono": "Teléfono",
        "producto": "Producto",
        "saldo_vencido": "Saldo Vencido",
        "saldo_liquidar": "Saldo a Liquidar",
    }
}


DIAS = list(range(1, 32))
MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
BAR_HEIGHT = [4760.574783233897, 4913.391795116627, 4163.514627274546, 3522.195014011441, 2191.986102855376, 210.07300825705215, 2948.2328239462854, 2306.854372344878, 926.2985805780119, 338.7208853603021, 2635.693908271509, 1608.7698764468914, 3853.586405786054, 3706.643790724449, 4516.192221472085, 2029.2884276548705, 4412.324945071792, 2983.2123279783964, 3394.8407383320864, 2688.352239058841, 1792.8816664580872, 3651.7500348438275, 4770.071671987543, 4170.3322956384745, 1797.547411865386, 2049.823508466561, 4716.411845719863, 3966.369831395647, 1175.1053130166506, 404.67298226116526, 2364.6135157308013]


COLORS = dict(primary = "#06417C", secondary = "#27A3D7")