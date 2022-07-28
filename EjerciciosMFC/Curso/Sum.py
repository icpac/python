
def miSum(*a):
    sum = 0
    for j in a:
        sum += j
    return sum


print(miSum(*[5, 6, 10, 12], 100))