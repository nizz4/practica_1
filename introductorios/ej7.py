oracion = input("Ingrese palabras: ")

lista= oracion.split()
print(lista)
listafinal = [i for i in lista if len(i)>3]
print(listafinal)