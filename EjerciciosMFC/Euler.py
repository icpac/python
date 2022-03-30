import math
from ntpath import join
import numpy as np
import scipy.special

# the two give the same results 
#val = scipy.special.binom(2*19, 19)
val = scipy.special.binom(2*4, 4)
print(f"binom 10 - 5: {val}")
val = math.factorial(2*19)/ (math.factorial(19) * math.factorial(19))
print(f"binom 10 - 5: {val}")


"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def SumaCadena2():
    cad = str(math.factorial(100))
    print("100!= ", cad)
    sum = 0
    for x in cad:
        sum += int(x)

    print("La suma es: ", sum)

def SumaFact():
    SumaCadena2()

def SumaCadena():
    cad = str(2**1000)
    print("2**1000= ", cad)
    sum = 0
    for x in cad:
        sum += int(x)

    print("La suma es: ", sum)

def DosAla():
    SumaCadena()
"""
37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690
"""

#"08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08",
"""
  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 
"""
listaNumbers = np.array([
"08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08",
"49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00",
"81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65",
"52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91",
"22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80",
"24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50",
"32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70",
"67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21",
"24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72",
"21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95",
"78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92",
"16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57",
"86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58",
"19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40",
"04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66",
"88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69",
"04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36",
"20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16",
"20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54",
"01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
])

def enPosxy(x, y):
    ren = listaNumbers[y-1]
    pos = (x-1)*3
    col = ren[pos:pos+2]
    return int(col)

def UpDown():
    maxProd = 0
    maxX = 0
    maxY = 0
    lenX = (len(listaNumbers[0])+1)//3
    lenY = len(listaNumbers)
    for x in range(lenX):
        for y in range(lenY):
            y1 = enPosxy(x+1, (y+1)%lenY)
            y2 = enPosxy(x+1, (y+2)%lenY)
            y3 = enPosxy(x+1, (y+3)%lenY)
            y4 = enPosxy(x+1, (y+4)%lenY)
            prodH = y1*y2*y3*y4
            if prodH > maxProd:
                maxProd = prodH
                maxX = x 
                maxY = y

    return maxProd, maxX+1, maxY+1
    """
    print("Maximo Producto:")
    print(maxProd)
    print("Maximo x, y")
    print(maxX+1, maxY+1)"""
    
def leftRight():
    maxProd = 0
    maxX = 0
    maxY = 0
    lenX = (len(listaNumbers[0])+1)//3
    lenY = len(listaNumbers)
    print("lenX:", lenX)
    for y in range(lenY):
        for x in range(lenX):
            v1 = enPosxy(x+1, y+1)
            px = x
            if x+2 > lenX:
                px = x-lenX
            v2 = enPosxy(px+2, y+1)
            px = x
            if x+3 > lenX:
                px = x-lenX
            v3 = enPosxy(px+3, y+1)
            px = x
            if x+4 > lenX:
                px = x-lenX
            v4 = enPosxy(px+4, y+1)
            prodH = v1*v2*v3*v4
            if prodH > maxProd:
                maxProd = prodH
                maxX = x 
                maxY = y

    return maxProd, maxX+1, maxY+1
    """
    print("Maximo Producto:")
    print(maxProd)
    print("Maximo x, y")
    print(maxX+1, maxY+1)"""
    
def dignal():
    maxProd = 0
    maxX = 0
    maxY = 0
    lenX = (len(listaNumbers[0])+1)//3
    lenY = len(listaNumbers)
    offset = 4
    #print("maxX:, maxY", lenX, lenY)
    for y in range(lenY-offset+1):
        for x in range(lenX-offset+1):
            v1 = enPosxy(x+1, y+1)
            v2 = enPosxy(x+2, y+2)
            v3 = enPosxy(x+3, y+3)
            v4 = enPosxy(x+4, y+4)
            prodH = v1*v2*v3*v4
            if prodH > maxProd:
                maxProd = prodH
                maxX = x 
                maxY = y

    return maxProd, maxX+1, maxY+1
    """
    print("Maximo Producto:")
    print(maxProd)
    print("Maximo x, y")
    print(maxX+1, maxY+1)
    return """

def dignalInver():
    maxProd = 0
    maxX = 0
    maxY = 0
    lenX = (len(listaNumbers[0])+1)//3
    lenY = len(listaNumbers)
    offset = 4
    for x in range(offset-1, lenX):
        for y in range(lenY-offset+1):
            v1 = enPosxy(x+1, y+1)
            v2 = enPosxy(x, y+2)
            v3 = enPosxy(x-1, y+3)
            v4 = enPosxy(x-2, y+4)
            prodH = v1*v2*v3*v4
            if prodH > maxProd:
                maxProd = prodH
                maxX = x 
                maxY = y

    return maxProd, maxX+1, maxY+1


def Prod4Numbers():
    res = UpDown()
    res1 = leftRight()
    res2 = dignal()
    res3 = dignalInver()

    x = res[1]
    y = res[2]
    max = res[0]
    if res1[0] >max:
        max = res1[0]
        x = res1[1]
        y = res1[2]
    if res2[0] > max:
        max = res2[0]
        x = res2[1]
        y = res2[2]
    if res3[0] > max:
        max = res3[0]
        x = res3[1]
        y = res3[2]

    print("Máximo producto\n", max)
    print("Posicion\n", x, y)


"""
¿Cuál es el mayor producto de cuatro números adyacentes en 
la misma dirección (arriba, abajo, izquierda, derecha o diagonal) 
en la cuadrícula de 20×20?
"08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08",
"49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00",
"81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65",
"52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91",
"22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80",
"24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50",
"32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70",
"67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21",
"24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72",
"21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95",
"78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92",
"16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57",
"86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58",
"19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40",
"04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66",
"88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69",
"04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36",
"20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16",
"20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54",
"01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
"""


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

def xmain():
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

def TestLat():
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