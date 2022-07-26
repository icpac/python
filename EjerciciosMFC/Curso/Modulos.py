
import time

def tt():
    for i in range(10):
        print(i)
        time.sleep(1)

    from time import sleep

    for j in range(5):
        print(j)
        sleep(1)


import random

print(random.randint(10, 15))
print(random.randint(-10, 20))
print(random.random())