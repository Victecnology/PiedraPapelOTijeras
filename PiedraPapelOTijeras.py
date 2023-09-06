import tkinter as tk
import random

# Constantes para las opciones del juego
PIEDRA = 1
PAPEL = 2
TIJERAS = 3

# Función para generar una opción aleatoria para la computadora
def generar_opcion_computadora():
    return int(random.random() * 3) + 1

# Función para comparar las opciones de los jugadores
def comparar_opciones(opcion_jugador, opcion_computadora):
    if opcion_jugador == opcion_computadora:
        return "Empate"
    elif opcion_jugador == PIEDRA and opcion_computadora == TIJERAS:
        return "Ganaste"
    elif opcion_jugador == PAPEL and opcion_computadora == PIEDRA:
        return "Ganaste"
    elif opcion_jugador == TIJERAS and opcion_jugador == PAPEL:
        return "Ganaste"
    else:
        return "Perdiste"

# Función para mostrar la interfaz de usuario
def mostrar_interfaz_usuario():
    root = tk.Tk()
    root.title("Piedra, Papel y Tijera")

    # Etiquetas para las opciones del juego
    label_piedra = tk.Label(root, text="Piedra")
    label_papel = tk.Label(root, text="Papel")
    label_tijeras = tk.Label(root, text="Tijeras")

    # Botones para las opciones del juego
    button_piedra = tk.Button(root, text="Piedra", command=lambda: jugar(PIEDRA))
    button_papel = tk.Button(root, text="Papel", command=lambda: jugar(PAPEL))
    button_tijeras = tk.Button(root, text="Tijeras", command=lambda: jugar(TIJERAS))

    # Colocar los elementos en la ventana
    label_piedra.grid(row=0, column=0)
    label_papel.grid(row=1, column=0)
    label_tijeras.grid(row=2, column=0)
    button_piedra.grid(row=0, column=1)
    button_papel.grid(row=1, column=1)
    button_tijeras.grid(row=2, column=1)

    root.mainloop()

# Función para jugar una partida
def jugar(opcion_jugador):
    # Obtener la opción de la computadora
    opcion_computadora = generar_opcion_computadora()

    # Mostrar el resultado de la partida
    result = comparar_opciones(opcion_jugador, opcion_computadora)
    print(f"La computadora sacó {opcion_computadora}. Tu opción fue {opcion_jugador}. El resultado es {result}.")

# Llamar a la función para mostrar la interfaz de usuario
mostrar_interfaz_usuario()