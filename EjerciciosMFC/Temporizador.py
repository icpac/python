
import time

nseg = 6
for i in range(nseg):
    print(i)
    time.sleep(1)

lista = []
lista.append("fuerza")
lista.append("padeciendo")
sub = lista[0:1]
sub[0] = 1
sub.insert(0, "crimen")
sub.insert(2, "amenazando")
print("Ya es hora")
print(lista)
print(lista[1])
print(lista[0:1])
print(lista)
print(sub)
sub.remove(1)
del sub[0]
print(sub)
item = sub.pop()
print(sub)
print(item)

sub.append("valor")
sub.insert(1, "compa")
sub.sort(reverse=True)
#sub.reverse()
print(sub)
sub.pop(1)
print(sub)

total = 10
def funcion(arg1):
    nuevo = total
    print(sub)
    print(arg1)
    print(nuevo)
    return

funcion("hola")
print(total)