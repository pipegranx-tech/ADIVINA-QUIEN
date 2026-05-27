RUTA_HISTORIAL = "data/historial.txt"
def guardar_resultado_partida(nombre_jugador, resultado, nombre_personaje, preguntas_usadas):
    """
    Almacena el resultado de una partida en el archivo de historial.
Si el archivo aún no existe, el programa lo crea de forma automática.
    """
    try:
        archivo = open(RUTA_HISTORIAL, "a", encoding="utf-8")
        linea = f"Jugador: {nombre_jugador} | Resultado: {resultado} | Personaje: {nombre_personaje} | Preguntas usadas: {preguntas_usadas}\n"
        archivo.write(linea)
        archivo.close()
        print("\n  Resultado guardado en el historial.")
    except Exception as e:
        print(f"\n  Cuidado: No se pudo guardar el historial. ({e})")
def mostrar_historial():
    """
    Carga y muestra todas las partidas almacenadas en el historial.
    """
    try:
        archivo = open(RUTA_HISTORIAL, "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()
    except FileNotFoundError:
        print("\n  No hay partidas archivadas en el historial aun.")
        return
    if len(lineas) == 0:
        print("\n  El historial esta vacio.")
        return
    print("\n" + "=" * 60)
    print("           HISTORIAL DE PARTIDAS")
    print("=" * 60)
    for i in range(len(lineas)):
        print(f"  {i + 1}. {lineas[i].strip()}")
    print("=" * 60)