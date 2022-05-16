nota1 = int (input())
nota2 = int (input())
nota3 = int (input())

# def promedio((a, b, c):
#     p = ( a + b  + c  ) / 2
#     return p

def notaFinal(a, b, c):
    nF = ( a * 0.20 + b * 0.50 + c * 0.30 )
    return nF

print (notaFinal( nota1, nota2, nota3 ))

if (notaFinal( nota1, nota2, nota3 ) >= 4):
    print("Aprobo")
else:
    print("No aprobo")