# Diseñar un programa que analiza si una frase es un pangrama del idioma inglés, es decir, si contiene todas las letras del alfabeto al menos 1 vez. El programa debe ser capaz de ignorar espacios y signos de puntuación. Por ejemplo:

# frase = "the quick brown fox jumps over the lazy dog"

# El siguiente set puede serles de utilidad:

# letras = set("abcdefghijklmnopqrstuvwxyz")

frase = "jackdaws love my big sphinx of quartz. "
splitFrase = frase.split()
texto = set({})

print(splitFrase)
for palabra in splitFrase:
    print(palabra)
    for caracter in palabra:
        print(caracter)
        texto.add(caracter)

print(texto)

letras = set("abcdefghijklmnopqrstuvwxyz")

def contador():
    cant = letras - texto
    print(cant)
    if cant == set():
        print ("La frase es un pangrama")
    else:
        print ("No es un pangrama")

contador()

# funciona pero habría que corregir mayúsculas y coin puntuacion anda pero no termino de entender porque