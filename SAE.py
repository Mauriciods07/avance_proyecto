#Declarar funciones

#Riqueza_lexica se encarga de contar el número de palabras de cada texto. Con el número que salga de la razón, se puede hacer una estimación
#Si el número es mayor a 1, los textos, posiblemente, pertenecen al mismo autor. Si el número es menor a 1, los textos no tienen una similitud muy amplia
def Riqueza_lexica():
    with open("Textos/texto01.txt", "r", encoding = 'utf8') as doc:
        texto1 = doc.read()
        dato1 =len(texto1) / len(set(texto1))
    with open("Textos/texto02.txt", "r", encoding = 'utf8') as doc:
        texto2 = doc.read()
        dato2 = len(texto2) / len(set(texto2))
    promedio = dato1 / dato2
    if promedio > 1:
        print("Los textos son semejantes")
    else:
        print("Los textos son distintos")
      
opcion = 0
while True:
    if opcion != 2:
        opcion = int(input())
    else:
        opcion = 3

    if opcion is 1:
        Riqueza_lexica()
    elif opcion is 2:
        print("Holi2")
    elif opcion is 3:
        break
    else:
        print("Opción no válida")
    print("¿Desea hacer otra prueba?")
    print("1. Sí")
    print("2. No")
    opcion = int(input())

print("Gracias por usar el servicio de SAE")