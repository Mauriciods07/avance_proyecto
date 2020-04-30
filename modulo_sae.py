#modulo en donde se encuentran lsa funciones del programa
import request

#Declarar funciones

def Etiquetado_POS():
    #Código copiado del servicio Freeling http://www.corpus.unam.mx/servicio-freeling/
    files = {'file': open('Textos/texto01.txt', 'rb')}
    params = {'outf': 'tagged', 'format': 'json'}
    url = "http://www.corpus.unam.mx/servicio-freeling/analyze.php"
    r = requests.post(url, files=files, params=params)
    obj1 = r.json()
    
    files = {'file': open('Textos/texto01.txt', 'rb')}
    params = {'outf': 'tagged', 'format': 'json'}
    url = "http://www.corpus.unam.mx/servicio-freeling/analyze.php"
    r = requests.post(url, files=files, params=params)
    obj2 = r.json()
    return obj1, obj2

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

#Esta función obtiene las palabras en común que tienen ambos textos y las divide entre la suma de las palabras totales de ambos textos
def Dice_similarity():
    cont = 0
    WORDS1 = []
    WORDS2 = []
    COMMON_WORDS = []
    token = 'token'
    lemma = 'lemma'
    i = 50
    
    for oracion in POS_TEXTO1:
        for palabra in oracion:
            WORDS1.append(palabra[lemma])
                
    for oracion in POS_TEXTO2:
        for palabra in oracion:
            WORDS2.append(palabra[lemma])
    
    for palabra in WORDS1:
        if palabra in WORDS2:
            if palabra not in COMMON_WORDS:
                cont = cont + 1
                COMMON_WORDS.append(palabra)

    print("comunes ", len(COMMON_WORDS))
    print("texto 1 ", len(WORDS1))
    print("texto 2 ", len(WORDS2))
    print("acercamiento "+str((len(COMMON_WORDS))/(len(WORDS1) + len(WORDS2) - len(COMMON_WORDS))))
    return (2*len(COMMON_WORDS))/(len(WORDS1) + len(WORDS2))