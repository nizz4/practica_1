secs = int(input("Escriba una cantidad de segundos: "))

minutos = (secs % 3600) // 60
horas = secs // 3600
segundos = secs % 60
print (segundos)
print (f'{secs} segundos equivale a {horas} horas, {minutos} minutos y {segundos} segundos')