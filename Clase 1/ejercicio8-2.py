# Escribir una función que recibe un número N y retorna la cantidad de divisores del mismo.
# Ejemplos:
# contarDivisores(9) → 3 (El número 9 tiene 3 divisores: 1, 3, 9)
# contarDivisores(10) → 4 (El número 10 tiene 4 divisores: 1, 2, 5, 10)

def contarDivisores(n):
    a = 1
    b = 0

    while n >= a:
        c = n % a
        a += 1
        if c == 0:
            b += 1
    print("Cantidad de divisores", b)
    return b
                

n = int (input("Ingrese un nùmero para averiguar sus divisores: "))

contarDivisores(n)