import numpy as np
import inflect


"""
Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an 
amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 
11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

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