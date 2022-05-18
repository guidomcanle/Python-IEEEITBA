a = [2*x for x in range(1, 25)]
print(a)

string = input("Ingresar un string: ")
index1 = int( input("Ingresar primer indice: "))
index2 = int( input("Ingresar segundo indice: "))

stringList = list(string)

stringList[index1], stringList[index2] =  stringList[index2], stringList[index1]

stringFinal = "".join(stringList)

print(stringFinal)