numeroPrimo = 11


"""
Questa funzione inizializza l'array con tutti gli
elementi a zero
"""
def initializeArray(array,p):

    #genero un array lungo quanto il numero e lo
    #inizializzo a 0
    for x in range (0,p-1):
        array.append(0)

"""
Tale funzione controlla l'array, se c'è un elemento inizializzato a zero
vale a dire che quel numero non è generatore
"""
def checkArray(array,p):
    isCorrect = True

    for index in range (1,p-1):
        if (array[index] == 0):
            isCorrect = False
            return isCorrect

    return isCorrect

"""
Metodo classico per la ricerca dei generatori
"""
def findGenerators(p):

    results = [0]
    generators = [0]

    #inizilizzo l'array
    initializeArray(results,p)

    x: int
    for x in range (2,p-1):
        for y in range (1,p):
            print('pow', x, ',', y)
            value = pow(x,y) % p
            print ('result',value)
            results[value] = value

        if checkArray(results,p) == True:
           generators.append(x)

    generators.remove(0)
    return generators

print ('il primo generatore trovato:',findGenerators(numeroPrimo))
