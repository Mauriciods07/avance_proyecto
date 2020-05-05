#bibliotecas
import nltk
from modulo_sae import *
import numpy


#Cuerpo del programa      
opcion = 0
POS_TEXTO1, POS_TEXTO2 = Etiquetado_POS()
valores = [0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3]

while True: 
    print("Bienvenido al SAE")
    #...
    opcion = int(input("¿Qué desea hacer?"))
    
    if opcion is 1:
        Riqueza_lexica()
    elif opcion is 2:
        Dice_similarity()
    elif opcion is 3:
        print("1. adjetivo")
        print("2. sustantivo")
        print("3. verbo")
        print("4. adverbio")
        print("5. determinante")
        POS = int(input("¿Qué categoría gramatical necesitas?: "))
        Contar_pos(POS)
    elif opcion is 4:
        break
    else:
        print("Opción no válida")
        
    print("¿Desea hacer otra prueba?")
    print("1. Sí")
    print("2. No")
    opcion = int(input())
    if opcion == 2:
        break

print("Gracias por usar el servicio de SAE")