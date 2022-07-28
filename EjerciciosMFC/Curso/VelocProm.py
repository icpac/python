
def prmVel():
    numI = 0
    sumT = 0
    while True:
        vlr = input("Tiempo para los 10 km: ")
        if not vlr:
            break

        sumT += float(vlr)
        numI += 1
        
    print(f"Promedio de tiempo: {sumT/numI} en {numI} corridas")



prmVel()
