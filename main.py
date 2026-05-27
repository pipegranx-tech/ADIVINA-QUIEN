from modulos import cargar_datos
from modulos import juego
from modulos import personajes
from modulos import archivos
RUTA_PERSONAJES = "data/personajes.txt"
def main():
    juego.mostrar_bienvenida()
    nombre_jugador = juego.pedir_nombre_jugador()
    print(f"\n  ¡Saludos, {nombre_jugador}! ¡Te deseo buena suerte!")
    lista_personajes = cargar_datos.leer_archivo_personajes(RUTA_PERSONAJES)
    if not cargar_datos.validar_personajes(lista_personajes):
        print("\n  El juego no se puede iniciar, hay errores en tus datos.")
        return
    archivos.mostrar_historial()
    personajes.mostrar_lista_personajes(lista_personajes)
    seguir_jugando = True
    while seguir_jugando:
        juego.iniciar_partida(lista_personajes, nombre_jugador)
        seguir_jugando = juego.preguntar_jugar_de_nuevo()
    print("\n" + "=" * 50)
    print(f"  ¡Nos vemos, {nombre_jugador}! ¡Gracias por participar!")
    print("=" * 50 + "\n")
if __name__ == "__main__":
    main()