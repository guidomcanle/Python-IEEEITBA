a = int (input("Ingrese un número: "))
b = int (input("Ingrese otro número mayor al anterior: "))

while a > b:
    print("El segundo número es mayor que el primero, ingreselos devuelta")
    a = int (input("Ingrese un número: "))
    b = int (input("Ingrese otro número mayor al anterior: "))

while a <= b:
    print(a)
    a += 1