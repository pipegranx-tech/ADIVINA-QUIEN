PREGUNTAS_DISPONIBLES = [
    {"texto": "¿Es mujer?",               "campo": "genero",   "valor": "femenino"},
    {"texto": "¿Es hombre?",              "campo": "genero",   "valor": "masculino"},
    {"texto": "¿Tiene gafas?",            "campo": "gafas",    "valor": "si"},
    {"texto": "¿Tiene sombrero?",         "campo": "sombrero", "valor": "si"},
    {"texto": "¿Tiene barba?",            "campo": "barba",    "valor": "si"},
    {"texto": "¿Tiene tatuaje?",          "campo": "tatuaje",  "valor": "si"},
    {"texto": "¿Tiene cabello negro?",    "campo": "cabello",  "valor": "negro"},
    {"texto": "¿Tiene cabello rubio?",    "campo": "cabello",  "valor": "rubio"},
    {"texto": "¿Tiene cabello castano?",  "campo": "cabello",  "valor": "castano"},
    {"texto": "¿Tiene cabello rojo?",     "campo": "cabello",  "valor": "rojo"},
    {"texto": "¿Tiene cabello canoso?",   "campo": "cabello",  "valor": "canoso"},
    {"texto": "¿Tiene ojos cafes?",       "campo": "ojos",     "valor": "cafes"},
    {"texto": "¿Tiene ojos azules?",      "campo": "ojos",     "valor": "azules"},
    {"texto": "¿Tiene ojos verdes?",      "campo": "ojos",     "valor": "verdes"},
]
def mostrar_menu_preguntas(preguntas_ya_hechas):
    """
    Muestra el menú de preguntas disponibles.
    Las preguntas que ya fueron hechas aparecen marcadas.
    Al final, agrega la opción de adivinar el personaje.
    """
    print("\n" + "-" * 50)
    print("  ¿Cual sera tu pregunta?")
    print("-" * 50)
    for i in range(len(PREGUNTAS_DISPONIBLES)):
        pregunta = PREGUNTAS_DISPONIBLES[i]
        if i in preguntas_ya_hechas:
            print(f"  {i + 1:2}. {pregunta['texto']}  [ya preguntado]")
        else:
            print(f"  {i + 1:2}. {pregunta['texto']}")
    print(f"  {len(PREGUNTAS_DISPONIBLES) + 1:2}. Intentar adivinar el personaje")
    print("-" * 50)
def recibir_opcion_usuario(total_opciones):
    """
    Pide al usuario que ingrese una opción del menú.
    Valida que sea un número dentro del rango permitido.
    Retorna el número de opción elegida (desde 1).
    """
    while True:
        entrada = input("  Tu opción: ").strip()
        if not entrada.isdigit():
            print("  Por favor ingresa un número válido.")
            continue
        opcion = int(entrada)
        if opcion < 1 or opcion > total_opciones:
            print(f"  Por favor ingresa un número entre 1 y {total_opciones}.")
            continue
        return opcion
def responder_pregunta(personaje_secreto, indice_pregunta):
    """
    Compara la pregunta elegida con las características del personaje secreto.
Devuelve "Sí" o "No" según corresponda.
    """
    pregunta = PREGUNTAS_DISPONIBLES[indice_pregunta]
    campo = pregunta["campo"]
    valor_esperado = pregunta["valor"]
    if campo not in personaje_secreto:
        return "No"
    valor_real = personaje_secreto[campo].lower()
    if valor_real == valor_esperado.lower():
        return "Sí"
    else:
        return "No"
def obtener_total_preguntas():
    """
    Devuelve la cantidad total de preguntas disponibles, sin incluir la opción de adivinar.
    """
    return len(PREGUNTAS_DISPONIBLES)