#Pedi que el juego sepa procesar empates y tambien que solicite un nombre al jugador
import random


def determinar_ganador(jugador, oponente):
    if jugador == oponente:
        return "empate"
    elif (jugador == "piedra" and oponente == "tijeras") or \
         (jugador == "tijeras" and oponente == "papel") or \
         (jugador == "papel" and oponente == "piedra"):
        return "jugador"
    else:
        return "oponente"


def juego_piedra_papel_tijeras():
    opciones = ["piedra", "papel", "tijeras"]

    nombre_jugador = input("Por favor, introduce tu nombre: ")
    print(f"Bienvenido, {nombre_jugador}!\n")

    while True:
        jugador = input(
            "Elige piedra, papel o tijeras (o 'salir' para terminar el juego): "
        ).lower()
        if jugador == "salir":
            print("¡Gracias por jugar!")
            break
        elif jugador not in opciones:
            print(
                "¡Opción no válida! Por favor, elige entre piedra, papel o tijeras."
            )
            continue

        oponente = random.choice(opciones)
        print("La elección del oponente es:", oponente)

        resultado = determinar_ganador(jugador, oponente)
        if resultado == "empate":
            print("¡Empate!")
        else:
            print(f"¡El ganador es: {nombre_jugador}!" if resultado ==
                  "jugador" else "¡El ganador es el oponente!")

        continuar = input("¿Quieres jugar de nuevo? (s/n): ")
        if continuar.lower() != "s":
            print("¡Gracias por jugar!")
            break


juego_piedra_papel_tijeras()