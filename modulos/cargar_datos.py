def leer_archivo_personajes(ruta_archivo):
    """
    Lee el archivo de personajes y devuelve una lista de diccionarios.
Cada diccionario contiene la información y características de un personaje.
    """
    personajes = []
    try:
        archivo = open(ruta_archivo, "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()
    except FileNotFoundError:
        print(f"Error: El archivo no existe '{ruta_archivo}'.")
        return []
    if len(lineas) == 0:
        print("Error: El archivo del personaje esta vacio.")
        return []
    encabezados = lineas[0].strip().split(",")
    for numero_linea in range(1, len(lineas)):
        linea = lineas[numero_linea].strip()
        if linea == "":
            continue
        valores = linea.split(",")
        if len(valores) != len(encabezados):
            print(f"Advertencia: La línea {numero_linea + 1} tiene datos incompletos y fue omitida.")
            continue
        personaje = {}
        for i in range(len(encabezados)):
            personaje[encabezados[i]] = valores[i]
        personajes.append(personaje)
    return personajes
def validar_personajes(lista_personajes):
    """
    Comprueba que la lista de personajes no esté vacía y que cada personaje
incluya al menos el campo “nombre”.
Devuelve True si la información es válida y False en caso contrario.
    """
    if len(lista_personajes) == 0:
        print("Error: No se cargaron personajes.")
        return False
    campos_requeridos = ["nombre", "genero", "cabello", "gafas", "sombrero", "barba", "ojos"]
    for personaje in lista_personajes:
        for campo in campos_requeridos:
            if campo not in personaje:
                print(f"Error: El personaje '{personaje.get('nombre', 'desconocido')}' no tiene el campo '{campo}'.")
                return False
    return True