
def Primos(qeNmro = 600851475143):
    listaPrimos = [2]
    limte = 10000 #600851475143
    numro = 3
    noEs = False
    maxmoPrimo = 1
    while numro <= limte:
        for i in listaPrimos:
            if numro % i == 0:
                noEs = True
                break

        if noEs == False:
            listaPrimos.append(numro)
            #if 600851475143 % numro == 0:
            #if 8462696833 % numro == 0:
            #if 10086647 % numro == 0:
            if qeNmro % numro == 0:
                maxmoPrimo = numro
                print(f"Factor: {numro}")
        numro += 2
        noEs = False

    print("El máximo que lo divide es:")
    print(maxmoPrimo)


numro = 998001
numro = 997799
numro = 996699
numro = 995599
numro = 994499
numro = 993399
numro = 992299
numro = 991199
990099
989989
988889
987789
986689
985589
984489
983389
Primos(numro)


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