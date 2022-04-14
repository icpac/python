from tkinter.tix import Tree
import numpy as np
import inflect
from sympy import divisors
from fractions import Fraction
import math
import itertools


def Permuta():
    for p in itertools.permutations(range(1, num)):
        print(p)

def LastPrim(ini, fin):
    for i in range(ini, fin, -1):
        pass


listaPrimos = [2]
def PrimosMenor2(listaPrimos=[2], inferior=3, limte=1000):
    numro = inferior
    noEs = False
    esquer = int(numro**(1/2))
    while numro < limte:
        for i in range(2, esquer+1):
            if numro % i == 0:
                noEs = True
                break 

        if noEs == False and numro < limte:
            listaPrimos.append(numro)

        numro += 2
        noEs = False
        esquer = int(numro**(1/2))


def PrimosMenor(listaPrimos=[2], limte=1000):
    numro = 3
    noEs = False
    esquer = numro**(1/2)
    while numro < limte:
        for i in listaPrimos:
            if numro % i == 0:
                noEs = True
                break 
            if i > esquer:
                break

        if noEs == False and numro < limte:
            listaPrimos.append(numro)

        numro += 2
        noEs = False
        esquer = numro**(1/2)

def PrimFile():
    nf = "EjerciciosMFC\ppam.txt"
    with open(nf) as f:
        lines = f.readlines()
    for l in lines:
        nmrs = l.split('\t')
        for n in nmrs:
            if len(n) > 1:
                listaPrimos.append(int(n))



def PanPrim(listaPrimos, minPrim):
    lstPanP = []
    for i in listaPrimos:
        if i > minPrim:
            istr = str(i)
            panP = True
            c = 1
            while c <= len(istr):
                cstr = str(c)
                nocurr = istr.count(cstr)
                if nocurr == 0 or nocurr > 1:
                    panP = False
                    break
                c += 1 
            
            if panP:
                lstPanP.append(i)

    return lstPanP



#PrimFile()
PrimosMenor2(listaPrimos,  899999999, 1000000000)
res = PanPrim(listaPrimos, 899999999)
print(res)

"""
12345678901234567890
10111213141516171819
20212223242526272829
30313233343536373839
40414243444546474849
50515253545556575859
60
70
80
90919293949596979899
100101102103104105106107108109
110
120
130
140
150
160
170
180
190

d1 = 1
d10 = 1
d100 = 5
d1 000  
d10 000 
d100 000 
d1 000 000
"""

def PosNum(numini, numfin, pos):
    strval = ""
    num = 0
    for i in range(numini, numfin+1):
        strval = strval+str(i)
        if pos <= len(strval):
            v = strval[pos-1]
            num = int(v)
            break
            
    return num

def ExePosNum():
    """https://oeis.org/A007376/b007376.txt"""
    #res = PosNum(1, 9, 5)
    #print(res)
    #res = PosNum(10, 99, 99-9)
    #print(res)
    res = PosNum(10, 99, 190-9)
    print(res)
    res = PosNum(100, 999, 1000-189)
    print(res)
    res = PosNum(1000, 9999, 10000-2889)
    print(res)
    res = PosNum(10000, 99999, 100000-42889)
    print(res)
    res = PosNum(100000, 999999, 1000000-492889)
    print(res)


def SolsPerm(n):
    lstSol = []
    for i in range(1, n):
        for j in range(1, n):
            if i+j < n:
                if i**2+j**2 == (n-i-j)**2:
                    lstSol.append(str(i)+", "+str(j)+", "+str(n-i-j))

    return lstSol

def Perims():
    maxPer = 0
    maxSols = 0
    maxRes = []
    for i in range(4, 1000+1):
        res = SolsPerm(i)
        if len(res) > maxSols:
            maxSols = len(res)
            maxPer = i
            maxRes = res

    print(maxSols) 
    print(maxPer)
    print(maxRes)





def TruncPrims(listaPrimos):
    lstTru = []
    for i in listaPrimos:
        istr = str(i)
        rp = True
        for j in range(1, len(istr)):
            isub = istr[j:]
            if int(isub) not in listaPrimos:
                rp = False
                break
        if rp:
            lp = True
            for j in range(1, len(istr)):
                isub = istr[:j]
                if int(isub) not in listaPrimos:
                    lp = False
                    break

        if rp and lp:
            lstTru.append(i)

    return lstTru


def TtPrim():
    PrimosMenor(listaPrimos, limte=1000000)
    res = TruncPrims(listaPrimos)
    print(res)


def isPalindrome(s):
    return s == s[::-1]

def PalDecBin(n):
    lstPalin = []
    for i in range(1, n):
        istr = str(i)
        if isPalindrome(istr):
            #ib = int(istr, 2)
            ib = bin(i).replace("0b", "")
            ibstr = str(ib)
            if isPalindrome(ibstr):
                lstPalin.append(i)

    return lstPalin

def PalDecBin():
    res = PalDecBin(1000000)
    print(sum(res))


def rotate(input,d): 
    # slice string in two parts for left and right 
    Lfirst = input[0 : d] 
    Lsecond = input[d :] 
  
    # now concatenate two parts together 
    return Lsecond + Lfirst

def PrimoCircular(listaPrimos):
    listCir = []
    for i in listaPrimos:
        primstr = str(i) 
        if (len(primstr) == 0):
            listCir.append(primstr)
        else:
            circP = True
            #if i == 101:
            #    circP = False
            auxprim = primstr
            for i in range(1, len(primstr)):
                auxprim = rotate(auxprim, 1)
                if int(auxprim) not in listaPrimos:
                    circP = False
                    break
            if circP:
                listCir.append(primstr)
    
    return listCir



def PCircular():
    PrimosMenor(listaPrimos, 1000000)
    res = PrimoCircular(listaPrimos)
    print(res)
    print(len(res))

def FactorialSum(n):
    listFacNum = []
    for i in range(n//2, n):
        numstr = str(i)
        sumfac = 0
        for c in numstr:
            cnum = int(c)
            sumfac = sumfac + math.factorial(cnum)
            if sumfac > i:
                break
        
        if i == sumfac:
            listFacNum.append(i)

    return listFacNum

def ff():
    res = FactorialSum(4194304*2*2*2*2)
    print(res)


def PanMul():
    multd = 1
    multr = 1
    lstPan = []

    for multd in range (3, 999):
        for multr in range(2, 9999):
            res = multd * multr
            multds = str(multd)
            multrs = str(multr)
            ress = str(res)
            if len(multds) + len(multrs) + len(ress) == 9:
                nvac = multds+multrs+ress
                cumple = Tree
                for c in "123456789":
                    if c not in nvac:
                        cumple = False
                        break
                if cumple:
                    lstPan.append(multds+"*"+multrs+"="+ress)

    
    return lstPan

def PanMulRes():
    res = PanMul()
    print(res)


def DigitCancel():
    num = 10
    den = num+1

    listVa = []
    while num <= 98:
        den = num +1
        while den <= 99:
            nums = str(num)
            dens = str(den)

            if (nums[0] == dens[0] or nums[0] == dens[1] 
            or nums[1] == dens[0] or nums[1] == dens[1]):
           
                val1 = num / den
                if nums[0] == dens[0]:
                    if int(dens[1]) != 0:
                        val2 = int(nums[1])/ int(dens[1])
                    else:
                        val2 = 0
                elif nums[0] == dens[1]:
                    if int(dens[0]) != 0:
                        val2 = int(nums[1])/ int(dens[0])
                    else:
                        val2 = 0
                elif nums[1] == dens[0]:
                    if int(dens[1]) != 0:
                        val2 = int(nums[0])/ int(dens[1])
                    else:
                        val2 = 0
                else:
                    if int(dens[0]) != 0:
                        val2 = int(nums[0])/ int(dens[0])
                    else:
                        val2 = 0

                if val1 == val2:
                    listVa.append(str(num)+"/"+str(den))

            den += 1
        num+= 1

    return listVa


def RedFracc():
    res = DigitCancel()
    print(res)


def QuintaPot(n, pot):
    listPt = []
    for i in range (n):
        text = str(i)
        val = 0
        for c in text:
            val = val + int(c)**pot

        if (i == val):
            listPt.append(i)

    return listPt

def CualesQuintaPor():
    res = QuintaPot(4194304, 5)
    print(res)


def numrosFibncci(n):
    nfibncci = 1
    f1 = 1
    f2 = 1
    while nfibncci <= n:
        if nfibncci == 1 or nfibncci == 2:
            nfibncci += 1
            yield 1
        else:
            nfibncci += 1
            fn = f2+f1
            f1 = f2
            f2 = fn
            yield fn

def mas1000():
    print("Esimo Fibonacci: ")
    tntos = 4782
    cual = 10**999
    for i in numrosFibncci(tntos):
        if i >= cual:
            print(i)

    

"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

Un número perfecto es un número para el cual la suma de sus 
divisores propios es exactamente igual al número. 
Por ejemplo, la suma de los divisores propios de 28 sería 
1 + 2 + 4 + 7 + 14 = 28, lo que significa que 28 es un 
número perfecto.
Un número n se llama deficiente si la suma de sus 
divisores propios es menor que n y 
abundante si esta suma excede de n.
Como 12 es el número abundante más pequeño, 
1 + 2 + 3 + 4 + 6 = 16, 
el número más pequeño que se puede escribir como 
la suma de dos números abundantes es 24. 
Mediante análisis matemático, se puede demostrar que 
todos los números enteros mayores que 28123 se puede escribir 
como la suma de dos números abundantes. 
Sin embargo, este límite superior no puede reducirse más 
mediante el análisis, aunque se sabe que el mayor número que 
no puede expresarse como la suma de dos números abundantes 
es menor que este límite.
Encuentra la suma de todos los números enteros positivos 
que no se pueden escribir como la suma de dos números abundantes.
"""
def CuntosPrimosCudrtca(a, b, listaPrimos):
    cuntos = 0
    i = 0
    while True:
        #if a == 1 and b == 41:
        #    print("Ohoh")
        px = i**2 + a*i + b
        if px not in listaPrimos:
            break
        else:
            cuntos += 1

        i += 1

    if px > listaPrimos[-1]:
        print(f"Px: {px}")
    return cuntos

def BuscaMaxCuadPrim(listaPrimos):
    maxCuntos = 0
    a = 1000
    ax = 0
    bx = 0
    for i in range(-a+1, a):
        for j in listaPrimos:
            if j < 1000:
                n = CuntosPrimosCudrtca(i, j, listaPrimos)
                if n > maxCuntos:
                    maxCuntos = n
                    ax = i
                    bx = j

    return maxCuntos, ax, bx

    

def CuadPrims():
    PrimosMenor(listaPrimos, 15001)
    res = BuscaMaxCuadPrim(listaPrimos)
    print(f"Cuantos Primos {res[0]}")
    print(f"Valor de a: {res[1]}")
    print(f"Valor de b: {res[2]}")

    #print(listaPrimos)






def Dignal(n):
    listDig = []
    print("Hello") 
    print(n)

    k = 1
    m = 1
    listDig.append(m)
    for i in range(1, (n+1)//2):
        for j in range(4):
            m = m+2*k
            listDig.append(m)
        k += 1

    return listDig


def SumDiag():
    res = Dignal(1001)
    print(sum(res))

def Decmal(n):
    frac = "0."
    pot = 10
    while n > pot:
        pot = pot*10
        frac = frac+"0"

    lstMod = [0]
    m = pot
    m1 = n
    while m%n != 0:
        frac = frac + str(m//n)
        if m%n in lstMod:
            break
        else:
            lstMod.append(m%n)
            m = m%n*10


    return frac

def MaxDecm():
    print(Decmal(14))

    num = 0
    tam = 0
    for i in range(1, 1001):
        lon = len(Decmal(i))
        if lon > tam:
            tam = lon
            num = i

    print("Tamano máximo:")
    print(f"Tamaño: {tam}")
    print(f"Número: {num}")
    print(f"Decimal: {Decmal(num)}")


#print(Fraction(0.09).limit_denominator())
#print(1/11)


#listaPrimos = [2]
def d(n):
    divsres = [1]
    lon = len(listaPrimos)

    i = 0
    while i < lon and listaPrimos[i] <= n//2:
        if n % listaPrimos[i] == 0:
            divsres.append(listaPrimos[i])
        i+=1

    if len(divsres) == 1 and n > 2:
        listaPrimos.append(n)
        return sum(divsres)
    else:
        todosDivsres = divsres.copy()
        k = 2
        for i in divsres[1:]:
            prm = i
            while prm**k < n:
                if n%prm**k == 0:
                    todosDivsres.append(prm**k)
                k += 1
            k = 2
        
        for j in divsres[1:]:
            for k in todosDivsres[1:]:
                if j*k <= n//2 and n%(j*k) == 0:
                    if j*k in todosDivsres:
                        pass
                    else:
                        todosDivsres.append(j*k)
        return sum(todosDivsres)

def SumaNOAbndntes(listaNumros, listaAbndntes):
    for i in listaNumros:
        if i > 0:
            suma = d(i)
            if suma > i:
                listaAbndntes.append(i)
    
    max = listaNumros[-1]
    for i in listaAbndntes:
        lista2 = [y+i for y in listaAbndntes]
        for k in lista2:
            if k <= max:
                listaNumros[k-1] = 0

    return sum(listaNumros)

def SumaNOA():
    # 28123
    listaAbndntes = []

    listaNumros = list(range(1, 28123+1))

    res = SumaNOAbndntes(listaNumros, listaAbndntes)
    print(listaNumros[:100])
    print(listaNumros)
    print(f"El resultado es: {res}")


def listNames():
    with open('EjerciciosMFC\p022_names.txt') as f:
        lines = f.readlines()

    Names = lines[0].split(",")
    Names.sort()

    sumaTotal = 0
    i = 0
    lon = len(Names)
    while i < lon:
        sumaName = 0
        for c in Names[i]:
            if c != '"':
                sumaName = sumaName+ord(c)-64
        sumaTotal = sumaTotal + (sumaName*(i+1))

        i+=1

    print(f"Suma Total: {sumaTotal}")



def SumaAmigbles(listaNumeros):
    sumaAmigbles = 0
    lon = len(listaNumeros)
    for i in listaNumeros:
        if i == 1184:
            lon = len(listaNumeros)
        if i > 0:
            suma = d(i)
            if suma > i:
                suma2 = d(suma)

                if i == suma2:
                    sumaAmigbles = sumaAmigbles + i + suma
                elif suma2 < i and suma-3 < lon: 
                    listaNumeros[suma-3] = 0
    
    return sumaAmigbles


def SumaAmigables():
                            #10000
    listaNumeros = list(range(3, 10000))
    res = SumaAmigbles(listaNumeros)

    print(f"El resultado es: {res}")

def Domngos():
    domngos = 0
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    nextDom = 1+6

    diasMes = 0
    domngosPrimro = 0
    signteDomngo = 1+6
    mesActal = 0
    ano = 1900
    while ano <= 2000:
        signteDomngo = signteDomngo + 7
        diasMes = meses[mesActal]
        if (ano%4 == 0) and mesActal == 1:
            diasMes += 1

        if signteDomngo > diasMes:
            signteDomngo = signteDomngo % diasMes
            mesActal += 1
        if signteDomngo == 1 and ano >= 1901:
            domngosPrimro += 1
        if mesActal >= 12:
            mesActal = 0
            ano += 1

    print(f"Cuantod domingos Primero= {domngosPrimro}")


def MayorPath():
    listTringlo = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20,  4, 82, 47, 65],
[19,  1, 23, 75,  3, 34],
[88,  2, 77, 73,  7, 63, 67],
[99, 65,  4, 28,  6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
]

    longtud = len(listTringlo)
    for i in range(longtud):
        if i > 0:
            for j in range(i+1):
                if j == 0:
                    listTringlo[i][j] = listTringlo[i][j] + listTringlo[i-1][j]
                else:
                    if j == i:
                        listTringlo[i][j] = listTringlo[i][j] + listTringlo[i-1][j-1]
                    else:
                        if listTringlo[i-1][j-1] > listTringlo[i-1][j]:
                            listTringlo[i][j] = listTringlo[i][j]+listTringlo[i-1][j-1]
                        else:
                            listTringlo[i][j] = listTringlo[i][j]+listTringlo[i-1][j]


    print(max(listTringlo[longtud-1]))


def NuberToPalabras():
    p = inflect.engine()
    longtud = 0
    ini = 1
    fin = 1000
    for i in range(ini, fin+1):
        text = p.number_to_words(i)
        longtud = longtud + len(text.replace(" ", "").replace("-", ""))

    print(text)
    print(longtud)





def Paths():
    np.set_printoptions(suppress=True)

    from math import factorial
    print(factorial(40)/(factorial(20))**2)

    tam = 21
    path = np.zeros((tam, tam))
    for r in range(tam):
        for c in range(tam):
            if c > 0:
                if r == 0:
                    path[r, c] = 1
                else:
                    path[r, c] = path[r-1, c] + path[r, c-1]
                    val = path[r, c]
            elif r > 0:
                path[r, c] = 1

    print(path)
    print(val)
