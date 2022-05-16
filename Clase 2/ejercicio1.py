# Crear:
#     Una función que convierta grados Celsius a grados Farenheit.
#     Una función que convierta grados Celsius a grados Kelvin.
# El usuario debe ingresar una temperatura en grados Celsius y el programa debe mostrar las conversiones a Farenheit y Kelvin utilizando las funciones. Si la temperatura ingresada es inferior al cero absoluto, el programa debe mostrar un mensaje de advertencia y pedir que se reingrese la temperatura.

c = float (input())

def aFarenheit(c):
    f = c * 9/5 + 32
    return f

print(round(aFarenheit(c), 2), "°F")

def aKelvin(c):
    k = c + 273.15 
    return k

print(round(aKelvin(c), 2), "°K")