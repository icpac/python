__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

from sympy import symbols, Eq, solve

x = symbols('x')

solc = solve(x**3 - 2*x**2+1)
print("Las soluciones de x**3 - 2x**2 + 1\n")
print(solc)

