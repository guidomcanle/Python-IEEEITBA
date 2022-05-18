file = open("noticia.txt", encoding="utf_8")

contenido = file.readlines()

palabras = []
no_deseado = ['\n', '"', ',', '.']

for line in contenido:
    # eliminamos los distintos carácteres no deseados uno por uno
    for caracter in no_deseado:
      line = line.replace(caracter,'')
    palabras_linea = line.split(' ') # separamos por espacios
    for palabra in palabras_linea: # por cada "string" separado por espacios
      if palabra != '':
        palabras.append(palabra.upper()) # convertimos todo a mayuscula

craterCant = 0
queCant = 0

for x in palabras:
    if x == "CRÁTER":
        craterCant += 1 

for z in palabras:
    if z == "QUE":
        queCant += 1 

print(craterCant)
print(queCant)