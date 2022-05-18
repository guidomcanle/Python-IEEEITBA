# Realizar un programa en el cual se decida el ganador de unas elecciones.

# El programa primero recibe un número N, la cantidad de votos totales que se realizaron. Luego recibe N votos en formato string, cada uno consiste en el nombre del candidato seleccionado. El programa debe calcular el ganador e imprimir su nombre. Para este ejemplo se asume que no hay empates. Los nombres y la cantidad de candidatos es desconocida.

from operator import itemgetter

cantVotos = int (input ())
votos = list()
votosD = {}

def sumarVotos():
    for i in range(cantVotos):
        agregar = input()
        votos.append(agregar)

def contarVotos():
    votosS = set(votos)
    for candidato in votosS:
        for voto in votos:
            if candidato == voto:
                votosD[candidato] = votosD.get(voto, 0) + 1

def sacarGanador():
    votosDOr = sorted(votosD.items(), key=itemgetter(1), reverse = True )
    print( votosDOr[0][0] )


sumarVotos()
contarVotos()
sacarGanador()