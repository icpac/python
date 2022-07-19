from random import randrange

with open('EjerciciosMFC\Frases.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

pos = randrange(len(lines))

print(pos)
print(lines[pos])