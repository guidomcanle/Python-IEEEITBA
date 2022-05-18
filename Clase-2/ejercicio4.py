#Realizar un programa que ordena nombres alfabéticamente. Primero debe pedir al usuario que ingrese la cantidad de nombres que serán ingresados. Luego debe pedir al usuario que ingrese un nombre y repetir ese pedido la cantidad de veces indicada. Dichos nombres deben ir agregandose a una lista. Por último, ordenar la lista alfabéticamente y mostrar en pantalla de a uno por vez los nombres ordenados.

cantidadDeNombres = int( input("Ingresar cantidad de nombres: "))
lista = []

while cantidadDeNombres != 0:
    agregar = input("Ingresar nombre: ")
    lista.append(agregar)
    cantidadDeNombres -= 1

lista.sort()

print(lista)