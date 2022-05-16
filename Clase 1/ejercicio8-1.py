# Escribir una función que chequee los siguientes usuarios y contraseñas:
# Usuario: Juan
# Contraseña: 12345_
# Usuario: Pablo
# Contraseña: xDcFvGbHn
# La función debe recibir como parámetros el usuario y la contraseña, y debe devolver el valor True o False.


def chequearUsuarioYContraseña (u,c):
    if u == usuario1 and c == constraseña1:
        resultado = True
    elif u == usuario2 and c == constraseña2:
        resultado = True
    else:
        print("Error al cargar el usuario o la contraseña")
        resultado = False
    return resultado


usuario1 = "Juan"
constraseña1 = "12345_"

usuario2 = "Pablo"
constraseña2 = "xDcFvGbHn"

u = input("Ingrese usuario: ")
c = input("Ingrese contraseña: ")        
while not chequearUsuarioYContraseña(u,c):
    u = input("Contraseña o usuarios incorrectos. Ingrese de nuevo el usuario:")
    c = input("Ahora la contraseña:")
else:
    print("Se ha loggeado correctamente")