# Escriba un programa que reciba un numero del usuario y repita el siguiente proceso usando un while:
#     Si el número es par, se debe dividir por 2.
#     Si el número es impar, se debe multiplicar por 3 y sumar 1.
# Este proceso se repite hasta llegar al numero 1 y luego muestra en pantalla la cantidad de pasos que tardó en llegar.
# Ejemplos:
#     Input: 6
#     Output: 8 (Los pasos a seguir son: 6, 3, 10, 5, 16, 8, 4, 2, 1)
#     Input: 13
#     Output: 9 (Los pasos a seguir son: 13, 40, 20, 10, 5, 16, 8, 4, 2, 1)

def lothar(x):
    pasos = 0
    while not x == 1:
        if x % 2 == 0:
            x /= 2
            pasos += 1
        else:
            x *= 3
            x += 1
            pasos += 1
    return int (pasos)

x = int (input())

print(lothar(x))