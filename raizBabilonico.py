# Carlos Javier López Cruz
# javier1604@gmail.com
#Método babilónico para encontrar una raíz cuadrada

totalIteraciones = 10
x0 = .5      # suposición inicial
raiz = 16    # número para sacar raíz 
itera = 1    # 
while itera < totalIteraciones:
    x = (1 / 2) * (x0 + raiz / x0)
    itera += 1
    x0 = x
    print(x)
    
