def mostrar_lista_personajes(lista_personajes):
    """
    Muestra en pantalla la lista de todos los personajes disponibles en el juego.
    """
    print("\n" + "=" * 50)
    print("       PERSONAJES DISPONIBLES")
    print("=" * 50)
    for i in range(len(lista_personajes)):
        nombre = lista_personajes[i]["nombre"]
        genero = lista_personajes[i]["genero"]
        print(f"  {i + 1:2}. {nombre} ({genero})")
    print("=" * 50)
def buscar_personaje_por_nombre(lista_personajes, nombre_buscado):
    """
    Busca un personaje en la lista utilizando su nombre, sin diferenciar entre mayúsculas y minúsculas.
Devuelve el diccionario del personaje si lo encuentra, o `None` si no existe.
    """
    nombre_buscado = nombre_buscado.strip().lower()
    for personaje in lista_personajes:
        if personaje["nombre"].lower() == nombre_buscado:
            return personaje
    return None
def verificar_nombre_existe(lista_personajes, nombre_ingresado):
    """
    Comprueba si el nombre ingresado por el usuario pertenece a algún personaje de la lista.
Devuelve `True` si existe y `False` en caso contrario.
    """
    personaje = buscar_personaje_por_nombre(lista_personajes, nombre_ingresado)
    return personaje is not None
def filtrar_personajes_por_caracteristica(lista_personajes, campo, valor):
    """
    Filtra y devuelve únicamente los personajes que poseen un valor específico en un campo determinado.
Por ejemplo: `campo="gafas"` y `valor="si"` devuelve solo los personajes que usan gafas.
    """
    personajes_filtrados = []
    for personaje in lista_personajes:
        if campo in personaje and personaje[campo].lower() == valor.lower():
            personajes_filtrados.append(personaje)
    return personajes_filtrados
def mostrar_personajes_posibles(lista_personajes_posibles):
    """
    Muestra la lista de personajes que aún podrían ser el personaje secreto.
    """
    if len(lista_personajes_posibles) == 0:
        print("  (No quedan personajes posibles)")
        return
    nombres = []
    for personaje in lista_personajes_posibles:
        nombres.append(personaje["nombre"])
    print(f"\n  Personajes que aún podrían ser: {', '.join(nombres)}")
def mostrar_caracteristicas_personaje(personaje):
    """
    Muestra todas las características de un personaje (se usa al final del juego).
    """
    print(f"\n  Nombre  : {personaje['nombre']}")
    print(f"  Género  : {personaje['genero']}")
    print(f"  Cabello : {personaje['cabello']}")
    print(f"  Gafas   : {personaje['gafas']}")
    print(f"  Sombrero: {personaje['sombrero']}")
    print(f"  Barba   : {personaje['barba']}")
    print(f"  Ojos    : {personaje['ojos']}")
    if "tatuaje" in personaje:
        print(f"  Tatuaje : {personaje['tatuaje']}")