nota = int (input("Ingrese su nota (del 0 al 10): "))

if nota <= 10 and nota >= 4:
    print('Aprobó')
elif nota <= 3 and nota >= 0:
    print("Reprobó")
else:
    print("El número ingresado es incorrecto")