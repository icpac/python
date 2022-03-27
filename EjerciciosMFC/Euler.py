import math



"""
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
"""


def PrimosMenor(listaPrimos=[2], limte=10001):
    suma = 2
    numro = 3
    noEs = False
    maxmoPrimo = 2
    while numro < limte:
        for i in listaPrimos:
            if numro % i == 0:
                noEs = True
                break 
            if i > numro//2:
                break

        if noEs == False and numro < limte:
            listaPrimos.append(numro)
            maxmoPrimo = numro
            suma = suma + numro

        numro += 2
        noEs = False
    
    return suma

suma = PrimosMenor(listaPrimos=[2], limte=2000000)
print("Suma:")
print(suma)

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

def PrimosNesimo(listaPrimos=[2], limte=10001):
    nesimo = 2
    numro = 3
    noEs = False
    maxmoPrimo = 1
    while nesimo <= limte:
        for i in listaPrimos:
            if numro % i == 0:
                noEs = True
                break

        if noEs == False:
            listaPrimos.append(numro)
            nesimo = nesimo+1
            maxmoPrimo = numro

        numro += 2
        noEs = False

    print("El enesimo primo es:")
    print(maxmoPrimo)

def PrimoNesimo():
    PrimosNesimo(listaPrimos=[2], limte=10001)

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