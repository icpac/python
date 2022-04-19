from fractions import Fraction
from operator import ne
import inflect
import itertools
import math
from ntpath import join
import numpy as np
from pyrsistent import b
import scipy.special
from sympy import divisors, isprime
from tkinter.tix import Tree


def WordsPen():
    nwp = 0
    nf = "EjerciciosMFC\p042_words.txt"
    with open(nf) as f:
        lines = f.readlines()
    for l in lines:
        nmrs = l.split(',')
        for n in nmrs:
            if len(n) > 1:
                print(n)

if __name__ == "__main__":
    WordsPen()
    print(ord("S")-ord("A")+1)
    print(ord("K")-ord("A")+1)
    print(ord("Y")-ord("A")+1)

def IsPrim(n):
    for i in range(2, int(n**(1/2))+2):
        if n%i == 0 and n > 2:
            return False
    return True

def ConseNoPrim(nc, lim):
    maxdiv = 4
    for i in range(nc, lim):
        if not IsPrim(i) and not isprime(i+1) \
            and not isprime(i+2) and not isprime(i+3):

            mi = i
            mi1 = i+1
            mi2 = i+2
            mi3 = i+3

            lstDiv = [0,0,0,0]
            lstDiv1 = [0,0,0,0]
            lstDiv2 = [0,0,0,0]
            lstDiv3 = [0,0,0,0]
            lstPrm = [0,0,0,0]
            lstPrm1 = [0,0,0,0]
            lstPrm2 = [0,0,0,0]
            lstPrm3 = [0,0,0,0]

            ne1 = -1
            ne2 = -1
            ne3 = -1
            ne4 = -1


            prVe = True
            while mi % 2 == 0:
                mi = mi//2
                if prVe:
                    ne1 += 1
                    prVe = False
                lstDiv[ne1] = lstDiv[ne1] + 1
                lstPrm[ne1] = 2

            prVe = True
            while mi1 % 2 == 0:
                mi1 = mi1//2
                if prVe:
                    ne2 += 1
                    prVe = False
                lstDiv1[ne2] = lstDiv1[ne2] + 1
                lstPrm1[ne2] = 2

            prVe = True
            while mi2 % 2 == 0:
                mi2 = mi2//2
                if prVe:
                    ne3 += 1
                    prVe = False
                lstDiv2[ne3] = lstDiv2[ne3] + 1
                lstPrm2[ne3] = 2

            prVe = True
            while mi3 % 2 == 0:
                mi3 = mi3//2
                if prVe:
                    ne4 += 1
                    prVe = False
                lstDiv3[ne4] = lstDiv3[ne4] + 1
                lstPrm3[ne4] = 2
            
            j = 3
            rd = (i+3)**(1/2) + 2
            while j < rd:
                if isprime(j):
                    
                    prVe = True
                    while mi % j == 0:
                        mi = mi//j
                        if prVe:
                            ne1 += 1
                            prVe = False
                            if ne1 > maxdiv-1:
                                break
                        lstDiv[ne1] = lstDiv[ne1] + 1
                        lstPrm[ne1] = j


                    prVe = True
                    while mi1 % j == 0:
                        mi1 = mi1//j
                        if prVe:
                            ne2 += 1
                            prVe = False
                            if ne2 > maxdiv-1:
                                break
                        lstDiv1[ne2] = lstDiv1[ne2] + 1
                        lstPrm1[ne2] = j


                    prVe = True
                    while mi2 % j == 0:
                        mi2 = mi2//j
                        if prVe:
                            ne3 += 1
                            prVe = False
                            if ne3 > maxdiv-1:
                                break
                        lstDiv2[ne3] = lstDiv2[ne3] + 1
                        lstPrm2[ne3] = j

                    prVe = True
                    while mi3 % j == 0:
                        mi3 = mi3//j 
                        if prVe:
                            ne4 += 1
                            prVe = False
                            if ne4 > maxdiv-1:
                                break
                        lstDiv3[ne4] = lstDiv3[ne4] + 1
                        lstPrm3[ne4] = j
                    
                    if ne1 >= maxdiv \
                        or ne2 >= maxdiv \
                        or ne3 >= maxdiv \
                            or ne4 >= maxdiv:
                        break
                j += 2

            if mi > 1 and ne1 < maxdiv-1:
                lstDiv[ne1+1] = mi
            if mi1 > 1 and ne2 < maxdiv-1:
                lstDiv1[ne2+1] = mi1
            if mi2 > 1 and ne3 < maxdiv-1:
                lstDiv2[ne3+1] = mi2
            if mi3 > 1 and ne4 < maxdiv-1:
                lstDiv3[ne4+1] = mi3
                 

            if 0 in lstDiv or 0 in lstDiv1 or 0 in lstDiv2 or 0 in lstDiv3:
                pass
            else:
                print("Este es el chido")
                print(i)
                print(lstDiv)
                print(lstPrm)
                print(lstDiv1)
                print(lstPrm1)
                print(lstDiv2)
                print(lstPrm2)
                print(lstDiv3)
                print(lstPrm3)



def ConseNoPrim():
    ConseNoPrim(100000, 300000)
    #ConseNoPrim(1, 188780)


def PotPot(n):
    sum = 0
    for i in range(1, n):
        sum += (i**i) % 100000000000
    print(sum)

def MainPot():
    PotPot(1000)



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
