
import random

print("Adivina el número !") 
ale = random.randint(1, 100)
num = ale+1
while num != ale:
    num = int(input("Qué número será ?"))
    if num < ale:
        print("Quedáste corto !")
    elif num > ale:
        print("Te excediste !")

if num == ale:
    print(f"Felicidades !\n el número era: {num}")


