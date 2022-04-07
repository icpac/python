import numpy as np
import inflect
from sympy import divisors
from fractions import Fraction

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

listaPrimos = [2]
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