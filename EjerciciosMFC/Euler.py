import math
from ntpath import join
import numpy as np


"""
¿Cuál es el mayor producto de cuatro números adyacentes en 
la misma dirección (arriba, abajo, izquierda, derecha o diagonal) 
en la cuadrícula de 20×20?
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""


lstnumros = [
"73167176531330624919225119674426574742355349194934", 
"96983520312774506326239578318016984801869478851843",
"85861560789112949495459501737958331952853208805511",
"12540698747158523863050715693290963295227443043557",
"66896648950445244523161731856403098711121722383113",
"62229893423380308135336276614282806444486645238749",
"30358907296290491560440772390713810515859307960866",
"70172427121883998797908792274921901699720888093776",
"65727333001053367881220235421809751254540594752243",
"52584907711670556013604839586446706324415722155397",
"53697817977846174064955149290862569321978468622482",
"83972241375657056057490261407972968652414535100474",
"82166370484403199890008895243450658541227588666881",
"16427171479924442928230863465674813919123162824586",
"17866458359124566529476545682848912883142607690042",
"24219022671055626321111109370544217506941658960408",
"07198403850962455444362981230987879927244284909188",
"84580156166097919133875499200524063689912560717606",
"05886116467109405077541002256983155200055935729725",
"71636269561882670428252483600823257530420752963450",
]
"""
 2 1 
 1 2
 2x2 = 2(2x1) = 1 = 2
 
 6 3 1
 3 4 3
 1 3 6 
 3x3 = 2(3x2) = 2(3x1+2x2) = 2(1+2)= 2*3 = 6
 2x3 = 3

 20  10   4  1
 10  12   9  4
  4   9  12 10 
  1   4  10 20 
2(4x3) = 2(4x2+3x3) = 2((4x1+3x2)+3x3)
3x2 = 3x1+2x2 = 1+2 = 3
= 2((1+3)+6) = 20

5x5 = 
2(5x4) = 2(5x3+4x4) = 2((5x2+4x3)+4x4)
2(((5x1+4x2)+(4x2+3x3))+4x4)

4x2 = 4x1+3x2
3x2 = 3x1 +2x2

 20  10  15   5  1
 10  12   9  16  5
 15   9  12  10  0 
  5   4  10  20  0
  1   0   0   0  0 
5x5 = 2 5x4 

 20  10  56  21  6  1
 10  12   9  16  5  0
 15   9  12  10  0  0
  5   4  10  20  0  0
  1   0   0   0  0  0
  0   0   0   0  0  0
5
 """


#function to calculate paths
def paths(n):
#apply the above stated rule for n iterations
    j = 1
    for i in range(1,n):
        j = j * (n + i) / i
    return j

def main():
  # input grid size
  p = paths(2);

#print paths
  print('The number of paths are:')
  print(p)

main()

def Lattce(ren, col):
    if col == ren:
        return 2*Lattce(ren, col-1)
    if col == 1:
        return 1
    if col > 1:
        if col+1 == ren:
            return Lattce(ren, col-1)+Lattce(col, col)
        else:
            return Lattce(ren, col-1)+Lattce(ren-1, col)
    else:
        return 0 

m = 20
#print (f"Lattice: \n {Lattce(m, m)}")

val = (math.factorial((m-1)*2))/ (math.factorial(m-1) * math.factorial(2*(m-1)-(m-1)))
print(f"Factorial = {val}")
"""
2 x 2 = 2!/1!(2-1)! = 2
3x3 = (3+1)! /2!(3-1)! = 24/4 = 6
4x4 = (4+2)!/3!(6-3)! = 6!/3!3! = 120/6 = 20
5x5 = (2(4-1))! / (4-1)! (2(4-1)-(4-1))!
       
4, 4 = 2(4, 3)
2(4x2+3x3) = 2((4x1+3x2)+3x3)
3x2 = 3x1+2x2 = 1+2 = 3
= 2((1+3)+6) = 20

3x3 = 2(3x2) = 2(3x1+2x2) = 2(1+2)= 2*3 = 6
 
2(4,4) = 
(4, 4) = 2(4,3 + 2(3,3))
4, 3 = 4,2
"""

def Collatz(numro):
    sec = 1
    print(numro)
    while numro > 1:
        if numro % 2 == 0:
            numro = numro // 2 
        else:
            numro = 3*numro + 1
        print(numro)
        sec += 1

    return sec

def MaxSecColl():
    nmmax = 0
    sec = 0
    for i in range(511000,1048576):
        nvsec = Collatz(i)
        if nvsec > sec:
            sec = nvsec
            nmmax = i

    print(f"maxima secuencia: {nmmax}")

def CalCollatz():
    print(f"maxima secuencia: {Collatz(837799)}")

def NumroTringlar(yesmo = 5):
    t = 1
    natral = 1
    while natral <= yesmo:
        yield t
        natral += 1
        t += natral


def MasDivsres():
    maxdiv = 0
    divisores = 0
    for i in NumroTringlar(12500):
        #if i%2 == 0 and i>:
        if i>66130750 and i%2 == 0:
            #print(i)
            divisores = 2
            for j in range(2, i//2+1):
                if i%j == 0:
                    divisores+=1
        
            #if divisores > maxdiv:
            #    maxdiv = divisores
            if divisores > 500:
                print(f"Este es el chido\n {i}")
                break

    print(i)
    print(f"Maximo divisores\n{maxdiv}")




def TernaPitagorica(numro = 1000):
    c = numro-3
    b = 2
    a = 1

    for i in range(numro):
        for j in range(numro-a):
            if a**2+b**2 == c**2:
                print("Esta es la terna:")
                print(a)
                print(b)
                print(c)
                break
            b += 1
            c = c-1
            if b >= c:
                break
        
        if a**2+b**2 == c**2:
            break
        
        a += 1
        b = a+1
        c = numro - a - b


def TernaPitagoricaMil():
    TernaPitagorica(numro = 1000)


def encntraProdcto(paso = 3):
    numros = ' '.join([str(item) for item in lstnumros])
    numros = numros.replace(" ", "")
    longtud = len(numros)

  
    #res = [''.join(sorted(numros[x:x+paso], reverse=True)) for x in range(longtud-paso)]
    res = np.array(["000"])

    for x in range (longtud-paso):
        sub = numros[x:x+paso]
        if sub.find("0") == -1:
            res = np.append(res, ''.join(sorted(numros[x:x+paso], reverse=True)))

    res = sorted(res)
    print("Longitud:")
    print(longtud)
    print("\nItems:")
    print(res)
    longtud = len(res)
    mul = 1
    for item in res:
        nwmul = 1
        for i in item:
            nwmul = nwmul * int(i)

        if nwmul > mul:
            mul = nwmul

    print("\nResultado:")
    print(mul) 

       

def SubcadenaProducto():
    encntraProdcto(paso=13)


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

def sumaPrimos():
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