
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square
from scipy import signal
from scipy.integrate import quad
from math import * 
"""import all function from math"""

"""x axis has been chosen from –π to +π, value """
x = np.arange(-np.pi, np.pi, 0.001) 

""" 
of 1 smallest square along x axis is 0.001 
defining square wave function 𝑦 =−1, 𝑓𝑜𝑟 − 𝜋 ≤ 𝑥 ≤ 0"""
y = square(x) 
#y = signal.sawtooth(2 * np.pi * 5 * t)
y = signal.sawtooth(2 * np.pi * 2 * x)
"""
y= +1, 𝑓𝑜𝑟 0 ≤ 𝑥 ≤ 𝜋
define fuction
"""

"""i :dummy index"""
fc = lambda x : square(x)*cos(i*x)  
fs = lambda x : square(x)*sin(i*x)

fc = lambda x : signal.sawtooth(2 * np.pi * 2 * x)*cos(i*x)
fs = lambda x : signal.sawtooth(2 * np.pi * 2 * x)*sin(i*x)
"""max value of I, not taken infinity, better result with high value"""
n = 50 

"""defining array"""
An = [] 
Bn = []

sum = 0
for i in range(n):
    an = quad(fc, -np.pi, np.pi)[0] * (1.0/np.pi)
    An.append(an)


for i in range(n):
    bn = quad(fs, -np.pi, np.pi)[0] * (1.0/np.pi)
    """putting value in array Bn"""
    Bn.append(bn) 

for i in range(n):
    if i==0.0:
        sum = sum + An[i]/2
    else:
        sum = sum + (An[i]*np.cos(i*x)+Bn[i]*np.sin(i*x))

plt.plot(x, sum, 'g')
plt.plot(x, y, 'r--')
plt.title("Serie de Fourier para una onda cuadrada")
plt.show()

