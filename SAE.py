#bibliotecas
import nltk
from modulo_sae import *
import numpy


#Cuerpo del programa      
opcion = 0
POS_TEXTO1, POS_TEXTO2 = Etiquetado_POS()
valores = [0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3]
lista = {}

while True: 
    print("Bienvenido al SAE")
    #...
    opcion = int(input("¿Qué desea hacer?"))
    
    if opcion is 1:
        lista["Riqueza léxica"] = Riqueza_lexica()
    elif opcion is 2:
        lista["Dice similarity"] = Dice_similarity()
    elif opcion is 3:
        print("1. adjetivo")
        print("2. sustantivo")
        print("3. verbo")
        print("4. adverbio")
        print("5. determinante")
        POS = int(input("¿Qué categoría gramatical necesitas?: "))
        texto, a = Contar_pos(POS)
        lista[texto] = a
    elif opcion is 4:
        datos = 0
        if len(list(lista)) <= 1:
            print("Se necesitan más datos para continuar")
            print("Por favor, haga otra prueba.")
        else:
            datos = sum(lista.values())
            resultado = promedio(datos, len(list(lista)))
            for elemento in list(lista):
                print("En {}, se obtuvo un resultado de {}".format(elemento, lista.get(elemento)))
            print("")
            print("El promedio de información analizada hasta el momento es igual a {}".format(resultado))
            print("Mientras más próximo esté el resultado a 1, más similitud existe entre los textos")
    elif opcion is 5:
        break
    else:
        print("Opción no válida")
        
    print("")
    print("¿Desea hacer otra prueba?")
    print("1. Sí")
    print("2. No")
    opcion = int(input())
    if opcion == 2:
        break
print("")
print("Gracias por usar el servicio de SAE")