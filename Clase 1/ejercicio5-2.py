nota = int (input("Ingrese su nota (del 0 al 100): "))

if nota <= 100 and nota >= 90:
    print('A')
elif nota <= 89 and nota >= 80:
    print('B')
elif nota <= 79 and nota >= 70:
    print('C')
elif nota <= 69 and nota >= 60:
    print('D')
elif nota <= 59 and nota >= 0:
    print('F')
else:
    print("El número ingresado es incorrecto")