# Realizar un programa que pida al usuario un número de legajo y el nombre completo, luego los guarde en un diccionario. En caso de que el número de legajo ya se encuentre en el diccionario, se debe mostrar un mensaje de advertencia.

# Usar dos celdas de código, en una crear el diccionario, y en la otra agregar el nombre y legajo y mostrar el contenido total. La idea es que cuando se ejecute varias veces la segunda celda se agrege un nuevo nombre y legajo a lo que ya había sido almacenado en el diccionario.

d = {14: "Juan"}

def agregarUsuario():
    legajo =  int(input ("Ingrese su legajo: "))
    nC =  input ("Ingrese su nombre completo: ")
    while legajo in d:
        legajo = int(input ("Ese legajo ya existe, ingrese uno nuevo: "))
    d[legajo] = nC

agregarUsuario()

print(d)
