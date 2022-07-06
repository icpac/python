import math


def CalculaDistancia(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)


def CalculaPerimetro(x1, x2, x3, x4,
    y1,y2, y3,y4):
    perimetro = 0
    perimetro += CalculaDistancia(0, 3, 3, 4)
    perimetro += CalculaDistancia(4, -1, 3, 4)
    perimetro += CalculaDistancia(4, -1, -3, -1)
    perimetro += CalculaDistancia(0, 3, -3, -1)
    return perimetro


#print("Calcula el Perimetro")
#print(CalculaPerimetro(-3, 0, 3, 4, -1, 3, 4, -1))

#print(12+2**(1/2)*(5**(1/2)+13**(1/2)))

#for i in range(1, 100):
#    print(i, math.log(i)/math.log(5)) 

print(math.log(25)/ math.log(5))
