# Se cuentan con varios sets que contienen nombres de personas a las que les gusta un cierto sabor de helado:

# vainilla = { "Juan", "Marina", "Tomas", "Paula" }
# chocolate = { "Pedro", "Paula", "Marina" }
# dulceDeLeche = { "Juan", "Julian", "Pedro", "Marina" }

# Responder, usando operaciones de sets:

#     ¿Hay alguna persona a la que le gusten todos los sabores?

#     ¿Hay alguna persona a la que le guste la vainilla y no el dulce de leche?

#     ¿Cuántas personas distintas tenemos?


vainilla = { "Juan", "Marina", "Tomas", "Paula" }
chocolate = { "Pedro", "Paula", "Marina" }
dulceDeLeche = { "Juan", "Julian", "Pedro", "Marina" }

def preg1():
    todosLosSabores = vainilla & chocolate & dulceDeLeche
    nombres = ", ".join(todosLosSabores)
    print("¿A alguien le gusta todos los sabores?")
    print("Sí, les gusta a:", nombres)


def preg2():
    vainillaYNoDll = vainilla - dulceDeLeche
    nombres = ", ".join(vainillaYNoDll)
    print("¿A alguien le gusta todo la vainilla pero aborrece el dulce de leche?")
    print("Sí, a: ", nombres)


def preg3():
    personas = vainilla | dulceDeLeche | chocolate
    nombres = ", ".join(personas)
    cant = len(personas)
    print("¿A alguien le gusta todo la vainilla pero aborrece el dulce de leche?")
    print("Sí, a: ", nombres,".", cant, "en total")


preg1()
preg2()
preg3()