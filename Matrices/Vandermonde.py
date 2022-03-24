
import numpy as np
import sympy as sp


a11,a12 = sp.symbols('a11,a12')

A = sp.Matrix([
[1,1,],
[a11,a12]])

L = sp.Matrix([
    [1, 0],
    [a11, 1]
])

U = sp.Matrix([
    [1, 1],
    [0, a12-a11]
])

#print(L*U)


a1,a2,a3 = sp.symbols('a1,a2,a3')

L = sp.Matrix([
    [1, 0, 0],
    [a1, 1, 0],
    [a1**2, a1+a2, 1]
])

U = sp.Matrix([
    [1, 1, 1],
    [0, a2-a1, a3-a1],
    [0, 0, (a3-a1)*(a3-a2)]
])

#print(sp.simplify(L*U))

a1,a2,a3,a4 = sp.symbols('a1,a2,a3,a4')

L = sp.Matrix([
    [1, 0, 0, 0],
    [a1, 1, 0, 0],
    [a1**2, a1+a2, 1,0],
    [a1**3, a2**2+a1*a2+a1**2, a3+a2+a1,1]
])

U = sp.Matrix([
    [1, 1,     1,               1],
    [0, a2-a1, a3-a1,           a4-a1],
    [0, 0,     (a3-a1)*(a3-a2), (a4-a1)*(a4-a2)],
    [0, 0,     0,               (a4-a1)*(a4-a2)*(a4-a3)]
#    [0, 0,     (a3-a1)*(a3-a2)*(a3+a2+a1),  (a4-a1)*(a4-a2)*(a4+a2+a1)]
])

#print(sp.simplify(L*U))


a1,a2,a3,a4,a5 = sp.symbols('a1,a2,a3,a4,a5')

L = sp.Matrix([
    [1,     0,                              0,                  0,           0],
    [a1,    1,                              0,                  0,           0],
    [a1**2, a1+a2,                          1,                  0,           0],
    [a1**3, a2**2+a1*a2+a1**2,              a3+a2+a1,           1,           0],
    [a1**4, a2**3+a1*a2**2+a1**2*a2+a1**3,  a1**2+a1*a2+a2**2+a3**2+a1*a3+a2*a3,  a4+a3+a2+a1, 1]
])

U = sp.Matrix([
    [1, 1,     1,               1,                       1],
    [0, a2-a1, a3-a1,           a4-a1,                   a5-a1],
    [0, 0,     (a3-a1)*(a3-a2), (a4-a1)*(a4-a2),         (a5-a1)*(a5-a2)],
    [0, 0,     0,               (a4-a1)*(a4-a2)*(a4-a3), (a5-a1)*(a5-a2)*(a5-a3)],
    [0, 0,     0,               0,                       (a5-a1)*(a5-a2)*(a5-a3)*(a5-a4)]
])

#print(sp.simplify(L*U))


a1,a2,a3,a4,a5,a6 = sp.symbols('a1,a2,a3,a4,a5,a6')

L = sp.Matrix([
    [1,     0,                                          0,                  0,           0,0],
    [a1,    1,                                          0,                  0,           0,0],
    [a1**2, a1+a2,                                      1,                  0,           0,0],
    [a1**3, a2**2+a1*a2+a1**2,                          a3+a2+a1,           1,           0,0],
    [a1**4, a2**3 + a1*a2**2 + a1**2*a2 +a1**3,         a1**2+a2**2+a3**2 +a1*a2+a1*a3+a2*a3,                                      a4+a3+a2+a1, 1,0],
    [a1**5, a2**4+a2**3*a1+a2**2*a1**2+a2*a1**3+a1**4,  a1**3+a2**3+a3**3+a1**2*a2+a1**2*a3+a2**2*a3+a1*a2**2+a1*a3**2+a2*a3**2+a1*a2*a3,  a1**2+a2**2+a3**2+a4**2+a1*a2+a1*a3+a1*a4+a2*a3+a2*a4+a3*a4, a5+a4+a3+a2+a1, 1]
])

U = sp.Matrix([
    [1, 1,     1,               1,                       1,                               1],
    [0, a2-a1, a3-a1,           a4-a1,                   a5-a1,                           a6-a1],
    [0, 0,     (a3-a1)*(a3-a2), (a4-a1)*(a4-a2),         (a5-a1)*(a5-a2),                 (a6-a1)*(a6-a2)],
    [0, 0,     0,               (a4-a1)*(a4-a2)*(a4-a3), (a5-a1)*(a5-a2)*(a5-a3),         (a6-a1)*(a6-a2)*(a6-a3)],
    [0, 0,     0,               0,                       (a5-a1)*(a5-a2)*(a5-a3)*(a5-a4), (a6-a1)*(a6-a2)*(a6-a3)*(a6-a4)],
    [0, 0,     0,               0,                       0,                               (a6-a1)*(a6-a2)*(a6-a3)*(a6-a4)*(a6-a5)]
])

#print(sp.simplify(L*U))

print(sp.simplify((a1**3-a2**3)/(a1-a2)))