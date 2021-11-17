import matplotlib.pyplot as plt


def funPar(n):
    """ n/2  """
    return n/2

def funImpar(n):
    """ (3n+1) / 2"""
    return (3*n+1)/2


def main(n):
    i = 1
    mientras = True
    while mientras:
        plt.plot(i, n, "o")
        if n % 2 == 0:
            n = funPar(n)
        else:
            n = funImpar(n)
        mientras = n != 1
        i = i+1
    plt.plot(i, n, "o")


for i in range(1, 180, 6):
    main(i+1)
plt.show()
    
