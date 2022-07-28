

def numExaToDec(num):
    for i, c in enumerate(reversed(num)):
        print(i, c)

    pot = len(num)-1
    value = 0
    for c in num:
        value += int(c)*16**pot
    
    return value

def numExa(num):
    resul = ""
    ent = int(num) 
    coc = 1

    while coc != 0:
        resid = ent % 16 
        coc = ent // 16
        if resid < 10:
            resul += str(resid)
        elif resid == 10:
            resul += "a"
        elif resid == 11:
            resul += "b"
        elif resid == 12:
            resul += "c"
        elif resid == 13:
            resul += "d"
        elif resid == 14:
            resul += "e"
        else:
            resul += "f"
        ent = coc

    return "0x" + resul.__reversed__


num = input("Que numero quiere convertir: ")
print(f"Número en Decimal {numExaToDec(num)}")