n = int(input("Ingrese un numero: "))

multiplos_5 = [i for i in range(1,n+1) if (i%5 == 0)]
no_multiplos_5 = [i for i in range(1,n+1) if (i%5 != 0)]
print (f'Multiplos de 5:   {multiplos_5}\nResto de números: {no_multiplos_5}')

