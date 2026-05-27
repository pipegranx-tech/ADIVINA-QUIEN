import random
from modulos import preguntas as mod_preguntas
from modulos import personajes as mod_personajes
from modulos import archivos as mod_archivos
LIMITE_PREGUNTAS = 10
def seleccionar_personaje_secreto(lista_personajes):
    """
    Elige un personaje al azar de la lista.
Devuelve el diccionario correspondiente al personaje seleccionado.
    """
    indice = random.randint(0, len(lista_personajes) - 1)
    return lista_personajes[indice]
def mostrar_bienvenida():
    """
    Enseña el mensaje de bienvenida al inicio del juego.
    """
    print("\n" + "_" * 50)
    print("     Bienvenido al juego: Adivina quien      ")
    print("_" * 50)
    print("  Estoy pensando en un personaje y debes adivinarlo.")
    print("  Utiliza preguntas clave para saber quien es.")
    print(f"  Tu limite son {LIMITE_PREGUNTAS} preguntas.")
    print("_" * 50)
def pedir_nombre_jugador():
    """
    Solicita al usuario que escriba su nombre.
Verifica que el campo no esté vacío.
Devuelve el nombre ingresado.
    """
    while True:
        nombre = input("\n  ¿Cuál es tu nombre? ").strip()
        if nombre != "":
            return nombre
        print("  El nombre no puede estar vacío.")
def ejecutar_turno(personaje_secreto, lista_personajes, preguntas_ya_hechas, personajes_posibles):
    """
    Realiza un turno del juego:

Muestra el menú de preguntas.
Recibe la opción seleccionada por el usuario.
Responde la pregunta o permite intentar adivinar, según la opción elegida.
Devuelve un diccionario con:
"accion": "pregunta" o "adivinar"
"gano": True o False (solo si la acción es "adivinar")
"preguntas_ya_hechas": conjunto actualizado
"personajes_posibles": lista actualizada
    """
    total_preguntas = mod_preguntas.obtener_total_preguntas()
    opcion_adivinar = total_preguntas + 1
    mod_preguntas.mostrar_menu_preguntas(preguntas_ya_hechas)
    mod_personajes.mostrar_personajes_posibles(personajes_posibles)
    print(f"\n  Preguntas restantes: {LIMITE_PREGUNTAS - len(preguntas_ya_hechas)}")
    opcion = mod_preguntas.recibir_opcion_usuario(opcion_adivinar)
    if opcion == opcion_adivinar:
        resultado = _resolver_adivinanza(personaje_secreto, lista_personajes)
        return {
            "accion": "adivinar",
            "gano": resultado,
            "preguntas_ya_hechas": preguntas_ya_hechas,
            "personajes_posibles": personajes_posibles
        }
    indice_pregunta = opcion - 1
    if indice_pregunta in preguntas_ya_hechas:
        print("\n  Ya hiciste esa pregunta antes. Elige otra.")
    else:
        respuesta = mod_preguntas.responder_pregunta(personaje_secreto, indice_pregunta)
        pregunta_texto = mod_preguntas.PREGUNTAS_DISPONIBLES[indice_pregunta]["texto"]
        print(f"\n  {pregunta_texto}  →  {respuesta}")
        preguntas_ya_hechas.add(indice_pregunta)
        campo = mod_preguntas.PREGUNTAS_DISPONIBLES[indice_pregunta]["campo"]
        valor = mod_preguntas.PREGUNTAS_DISPONIBLES[indice_pregunta]["valor"]
        if respuesta == "Sí":
            personajes_posibles = mod_personajes.filtrar_personajes_por_caracteristica(
                personajes_posibles, campo, valor
            )
        else:
            personajes_posibles = _filtrar_personajes_sin_caracteristica(
                personajes_posibles, campo, valor
            )
    return {
        "accion": "pregunta",
        "gano": False,
        "preguntas_ya_hechas": preguntas_ya_hechas,
        "personajes_posibles": personajes_posibles
    }
def _filtrar_personajes_sin_caracteristica(lista_personajes, campo, valor):
    """
    Devuelve los personajes que no poseen el valor especificado en el campo indicado.
    """
    resultado = []
    for personaje in lista_personajes:
        if campo in personaje and personaje[campo].lower() != valor.lower():
            resultado.append(personaje)
    return resultado
def _resolver_adivinanza(personaje_secreto, lista_personajes):
    """
    Solicita al usuario que ingrese el nombre del personaje que piensa que es el secreto.
Devuelve `True` si acierta y `False` en caso contrario.
    """
    print("\n  Escribe el nombre del personaje que crees que es:")
    nombre_intento = input("  Tu respuesta: ").strip()
    if not mod_personajes.verificar_nombre_existe(lista_personajes, nombre_intento):
        print(f"\n  '{nombre_intento}' no está en la lista de personajes.")
        return False
    nombre_secreto = personaje_secreto["nombre"].lower()
    nombre_intento_lower = nombre_intento.lower()
    return nombre_secreto == nombre_intento_lower
def iniciar_partida(lista_personajes, nombre_jugador):
    """
    Administra el desarrollo completo de la partida:

* Selecciona el personaje secreto.
* Ejecuta los turnos hasta que el usuario adivine o ya no queden preguntas disponibles.
* Muestra el resultado final.
* Guarda el resultado en el historial.
    """
    personaje_secreto = seleccionar_personaje_secreto(lista_personajes)
    preguntas_ya_hechas = set()
    personajes_posibles = list(lista_personajes)
    gano = False
    termino = False
    while not termino:
        resultado_turno = ejecutar_turno(
            personaje_secreto,
            lista_personajes,
            preguntas_ya_hechas,
            personajes_posibles
        )
        preguntas_ya_hechas = resultado_turno["preguntas_ya_hechas"]
        personajes_posibles = resultado_turno["personajes_posibles"]
        if resultado_turno["accion"] == "adivinar":
            gano = resultado_turno["gano"]
            termino = True
        elif len(preguntas_ya_hechas) >= LIMITE_PREGUNTAS:
            print(f"\n  ¡Se acabaron tus {LIMITE_PREGUNTAS} preguntas!")
            termino = True
    _mostrar_resultado_final(gano, personaje_secreto, nombre_jugador, len(preguntas_ya_hechas))
    resultado_texto = "ganó" if gano else "perdió"
    mod_archivos.guardar_resultado_partida(
        nombre_jugador,
        resultado_texto,
        personaje_secreto["nombre"],
        len(preguntas_ya_hechas)
    )
    return gano
def _mostrar_resultado_final(gano, personaje_secreto, nombre_jugador, preguntas_usadas):
    """
    Muestra el mensaje de resultado al terminar la partida.
    """
    print("\n" + "_" * 50)
    if gano:
        print(f"  ¡Bien hecho, {nombre_jugador}! ¡GANASTE! 🎉")
        print(f"  Adivinaste al personaje en {preguntas_usadas} pregunta(s).")
    else:
        print(f"  ¡Lo lamento, {nombre_jugador}! Perdiste.")
        print(f"  El personaje secreto era:")
        mod_personajes.mostrar_caracteristicas_personaje(personaje_secreto)
    print("_" * 50)
def preguntar_jugar_de_nuevo():
    """
   Consulta al usuario si desea iniciar otra partida.
Devuelve `True` si quiere volver a jugar y `False` en caso contrario.
    """
    while True:
        respuesta = input("\n  ¿Deseas jugar de nuevo? (s/n): ").strip().lower()
        if respuesta == "s":
            return True
        elif respuesta == "n":
            return False
        else:
            print("  Por favor ingresa 's' para sí o 'n' para no.")