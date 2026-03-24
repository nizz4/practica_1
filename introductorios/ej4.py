num = int(input('Ingrese un numero: '))

multiplos_no_5 = [i for i in range(1,num+1) if i%5 != 0]
print(multiplos_no_5)