# Carlos Javier López Cruz
# javier1604@gmail.com
#Método babilónico para encontrar una raíz cuadrada

totalIteraciones = 20
x0 = 10      # suposición inicial, siempre > 0
raiz = 17    # número al que se le sacará raíz 
itera = 1    # 
sufAprox = 0.000001 # suficiente aproximación

while itera < totalIteraciones and abs(x0 - raiz / x0) > sufAprox:
    x = (1 / 2) * (x0 + raiz / x0)
    x0 = x
    itera += 1

print("Cuantas iteraciones: ", itera) 
print("Raíz de: ", raiz, "= ", x)
    
