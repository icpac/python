import numpy as np
import inflect

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