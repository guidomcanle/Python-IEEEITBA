# Realizar un programa que decodifique código morse. El usuario debe ingresar una palabra en código morse, usando una secuencia de puntos, guiones y espacios como la siguiente:
# .--. .-. --- --. .-. .- -- .- -.-. .. --- -.
# Luego, separando por espacios, cada letra debe ser convertida de morse a una letra del alfabeto, y por último la traducción se muestra en pantalla como un string. Les proponemos definir un diccionario que ayude a realizar la traducción. Es importante considerar qué dato será la clave, y cuál el contenido, de forma en que les sea más útil para lograr resolver el desafío.
# Tips: Revisar los métodos .split() y .join() para convertir entre strings y listas.

codigoMorse = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", 
    "g": "--.", "h": "....", "i": "..", "j": "·---", "k": "-.-", "l": ".-..", 
    "m": "--", "n": "-.", "ñ": "--.--", "o": "---", "p": ".__.", "q": "--.-",
    "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
    "x": "-..-", "y": "-.--", "z": "--..",
    
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", 
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    
    ".": ".-.-.-", ",": "-.-.--", "?": "..--..", "\"": ".-..-.", " ":"/"
}

textoMorse = input("Escriba su fase en código morse: ")
texto = []

def trad():
    listMorse = textoMorse.split()
    for codigo in listMorse:
        for letraE in codigoMorse:
            if codigoMorse[letraE] == codigo:
                texto.append(letraE)
    textoStr = "".join(texto)
    print(textoMorse)
    print(textoStr)

trad()