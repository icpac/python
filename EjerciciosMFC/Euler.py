import math


def Primos(qeNmro = 600851475143, listaPrimos=[2]):
    limte = 100000 #600851475143
    numro = 3
    noEs = False
    maxmoPrimo = 1
    esPrio = False
    while numro <= limte:
        for i in listaPrimos:
            if numro == i:
                esPrimo = True
                break
            if numro % i == 0:
                noEs = True
                break

        if noEs == False:
            listaPrimos.append(numro)
            esPrimo = True
            #if 600851475143 % numro == 0:
            #if 8462696833 % numro == 0:
            #if 10086647 % numro == 0:
        if esPrimo:
            if qeNmro % numro == 0:
                maxmoPrimo = numro
                print(f"Factor: {numro}")
        numro += 2
        noEs = False
        esPrimo = False

    print("El máximo que lo divide es:")
    print(maxmoPrimo)


def Palindromo():
    # 999*999 = 998001
    numro = 998001
    numro = 997799

    listaPrimos = [2]
    numro = 997
    for i in range(997,900, -1):
        partes = numro 
        entfrac = math.modf(partes/10)
        partDere = entfrac[0]*1000
        partes = entfrac[1]
        entfrac = math.modf(partes/10)
        partDere = partDere + entfrac[0]*100
        partes = entfrac[1]
        entfrac = math.modf(partes/10)
        partDere = partDere + entfrac[0]*10

        numro = int(numro*1000 + partDere)
        print(numro)
        print(Primos(numro,listaPrimos))
        print("")
        numro = i




def fibncci():
    limte = 4000000
    termno1 = 1 
    termno2 = 2
    sumaPares = 0
    while termno1 <= limte or termno2 <= limte:
        if termno1 < limte and termno1 % 2 == 0:
            sumaPares += termno1
        if termno2 < limte and termno2 % 2 == 0:
            sumaPares += termno2
        termno1 = termno1 + termno2
        termno2 = termno2 + termno1

    print("Suma de Pares:")
    print(sumaPares)

def sum35():
    sum = 0
    limte = 1000
    for i in range(limte):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    print(sum) 