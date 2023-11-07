#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

def juego(ele_ju, puntaje_jug, puntaje_maq):
    opciones = ["piedra","papel","tijera"]

    if ele_ju in opciones:
        ele_maq = random.choice(opciones)
        if (ele_ju == "papel" and ele_maq == "piedra") or (ele_ju == "tijera" and ele_maq == "papel") or (ele_ju == "piedra" and ele_maq == "tijera"):
            print(f"la maquina eligio: {ele_maq}")
            print(f"{ele_ju} le gana a {ele_maq}. Ganaste un punto")
            puntaje_jug += 1
        
        elif (ele_ju == "papel" and ele_maq == "papel") or (ele_ju == "tijera" and ele_maq == "tijera") or (ele_ju == "piedra" and ele_maq == "piedra"):
            print(f"la maquina eligio: {ele_maq}")
            print(f"{ele_ju} es igual a {ele_maq}. No hay puntos")
        else:
            print(f"la maquina eligio: {ele_maq}")
            print(f"{ele_maq} le gana a {ele_ju}. La maquina gana un punto")
            puntaje_maq += 1

        print("   ")
        print("Si desea seguir jugando escriba 's' de lo contrario 'n'")
        seguir_jugando = input("Ingrese una opcion: ")
        if seguir_jugando == "s":
            print("   ")
            print ("Seleccione alguna de estas opciones: piedra, papel o tijera")
            opcion = input ("Ingrese alguna de las opciones de arriba: ")
            juego(opcion, puntaje_jug, puntaje_maq)

        elif seguir_jugando == "n":
            print("   ")
            print(f"Puntos maquina: {puntaje_maq}")
            print(f"Tus Puntos: {puntaje_jug}")
        
        else:
            print("Saliste del juego jejeje")
    else:
        print("La opcion no es valida. Intente otra vez")
        print("\n")
        eleccion_jugador = input ("Ingrese nuevamente una opcion valida: ")
        juego(eleccion_jugador, puntaje_jug, puntaje_maq)

print ("Debe seleccionar alguna de estas opciones: piedra, papel o tijera")
eleccion_jugador = input ("Ingrese alguna de las opciones de arriba: ")
juego(eleccion_jugador, 0, 0)
