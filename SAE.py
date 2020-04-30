#bibliotecas
import nltk
from modulo_sae import *


#Cuerpo del programa      
opcion = 0
POS_TEXTO1, POS_TEXTO2 = Etiquetado_POS()

while True: 
    print("Bienvenido al SAE")

    print("¿Qué desea hacer?")
    if opcion is 1:
        Riqueza_lexica()
    elif opcion is 2:
        Dice_similarity()
    elif opcion is 3:
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