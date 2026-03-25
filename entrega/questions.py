import random
categorias = {"PROGRAMACION": ["python", "programa", "variable", "funcion", "bucle"],
              "PAISES": ["argentina","chile","mexico","peru","uruguay","colombia"],
              "FRUTAS": ["banana","manzana","sandia","naranja","durazno","kiwi"],
              }

score = 0

print("¡Bienvenido al Ahorcado!")
print()
print("Categorías disponibles: ") 
for elem in categorias:
    print(f'* {elem}')
seleccion = input("\nElija una categoría antes de comenzar: ").upper()


while seleccion not in categorias:
         print(f"Categoría inexistente, elija otra: ")
         seleccion = input().upper()
palabras_elegidas = random.sample(categorias[seleccion], k=len(categorias[seleccion]))
print(f'\n- Categoria seleccionada: {seleccion} -\n')
for word in palabras_elegidas:
    guessed = []
    attempts = 6
    while attempts > 0:
         # Mostrar progreso: letras adivinadas y guiones para las que faltan
         progress = ""
         for letter in word:
             if letter in guessed:
                 progress += letter + " "
             else:
                 progress += "_ "
         print(progress)
         # Verificar si el jugador ya adivinó la palabra completa
         if "_" not in progress:
             print("¡Ganaste!")
             score= score+6
             break
         print(f"Intentos restantes: {attempts}")
         print(f"Letras usadas: {', '.join(guessed)}")
         letter = input("Ingresá una letra: ").lower()
         if letter.isalpha() and len(letter)==1:
             if letter in guessed:
                print("Ya usaste esa letra.")
             elif letter in word:
                 guessed.append(letter)
                 print("¡Bien! Esa letra está en la palabra.")
             else:
                 guessed.append(letter)
                 attempts -= 1
                 score -= 1
                 print("Esa letra no está en la palabra.")
         else:
             print("Entrada no válida")
         print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        score = 0
    print(f'Tu puntaje actual es de {score} puntos')
    if input(f'\n¿Jugar nuevamente? (si/no): ').lower() != "si":
        break
else:
    print(f"Se terminaron las palabras de {seleccion}. ¡Gracias por jugar!")
print(f'\n**¡Obtuviste un total de {score} puntos!**\n')