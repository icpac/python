from fractions import Fraction
import inflect
import itertools
import math
from ntpath import join
import numpy as np
import scipy.special
from sympy import divisors, isprime
from tkinter.tix import Tree


def PotPot(n):
    sum = 0
    for i in range(1, n):
        #print(i, i**i)
        sum += (i**i) % 100000000000
    print(sum)

if __name__ == "__main__":
    PotPot(1000)


def IsPrim(n):
    for i in range(2, int(n**(1/2))+2):
        if n%i == 0 and n > 2:
            return False
    return True

def ConsecutivePrime(m, lim, maxS):
    lstConse = []
    lstMax = []
    sumPr = 0
    maxPrim = 0
    i = m
    ns = 0
    maxsumnds = maxS
    mmxP = 0
    while i < lim:
        if IsPrim(i):
            sumPr += i            
            ns += 1
            lstConse.append(i)
            if ns >= maxsumnds or sumPr > lim:
                if sumPr > lim:
                    break
                if IsPrim(sumPr):
                    if ns > mmxP:
                        mmxP = ns
                        maxPrim = sumPr                        
                        lstMax = lstConse.copy()
                        
                lstConse.clear()
                sumPr = 0
                i = m
                ns = 0
                maxsumnds += 1
                continue
        if i%2 == 0:
            i += 1
        else:
            i += 2
    
    return maxPrim, lstMax, mmxP

def PrimSumConse():
    max = 0
    for i in range(2, 1000000):
        if IsPrim(i):
            res = ConsecutivePrime(i, 1000000, max)            
            if int(res[2]) > max:
                max = int(res[2])
                print(res[0], res[1], res[2])
                print("\n")


def PrimPerm(n):
    lstTal = []
    ctPr = 0
    if IsPrim(n):
        ctPr += 1
        for pr in itertools.permutations(str(n)):
            cad = ""
            for p in pr:
                cad += p

            if int(cad) > 999 and IsPrim(int(cad)):
                ctPr += 1
                if ctPr >= 3:
                    if int(cad) not in lstTal:
                        lstTal.append(int(cad))

    if len(lstTal) > 2:
        lstTal.sort()

        if len(lstTal) == 3:
            if lstTal[1] - lstTal[0] == lstTal[2] - lstTal[1]:
                print(lstTal)
        elif len(lstTal) == 4:
            if lstTal[1] - lstTal[0] == lstTal[2] - lstTal[1] \
             or lstTal[1] - lstTal[0] == lstTal[3] - lstTal[1] \
             or lstTal[2] - lstTal[0] == lstTal[3] - lstTal[2] \
             or lstTal[2] - lstTal[1] == lstTal[3] - lstTal[2]:
             print(lstTal)
        else:            
            print(lstTal)

def PrimPerm():
    for i in range(999+1, 9999+1):
        PrimPerm(i)






def edu_roots(a, b, c):  
    dis = (b**2) - (4*a*c)

    if dis > 0:
        root1 = (-b + math.sqrt(dis)) / (2 * a)
        root2 = (-b - math.sqrt(dis)) / (2 * a)
        return root1, root2

    elif(dis == 0):
        root1 = root2 = -b / (2 * a)
        return root1, root2

    elif(dis < 0):
        root1 = root2 = -b / (2 * a)
        imaginary = math.sqrt(-dis) / (2 * a)
        return root1, root2


def numrosPenta(n):
    return n*(3*n-1)/2


def VesiesP(sumP):
    res = edu_roots(3, -1, -2*sumP)
    if res[0] > 0  or res[1] > 0:
        if res[0] > 0:
            m = int(res[0])
            if sumP == numrosPenta(m):
                return True
        if res[1] > 0:
            m = int(res[1])
            if sumP == numrosPenta(m):
                return True
    return False

def listaPenta():
    lstPenSD = []
    for k in range(1, 4000):
        for i in range(1, 4000):
            nk = numrosPenta(k)
            ni = numrosPenta(i)
            if ni > nk:
                sumP = nk+ni
                if VesiesP(sumP):
                    resP = ni-nk
                    if resP > 0 and VesiesP(resP):
                        lstPenSD.append(str(int(ni))+"-"+str(int(nk)))

    return lstPenSD

def MinDifPenta():
    res = listaPenta()
    print(res)
