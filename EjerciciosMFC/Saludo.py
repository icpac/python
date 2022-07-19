
__autor__ = "Tlacaelel iCPAC"

from datetime import date, datetime
import pytz

fases = ["Luna creciente", "Cuarto creciente", 
"Creciente convexa", "Luna llena", 
"Menguante convexa", "Cuarto menguante", 
"Menguante cóncava", "Nueva"]


def FraseDia():
    from random import randrange

    with open('EjerciciosMFC\Frases.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    pos = randrange(len(lines))
    print(lines[pos])

def moon_phase(year, month, day):
    d = day;
    if month == 2:
        d += 31
    elif month > 2:
        d += 59+(month-3)*30.6+0.5
 
    g = (year-1900)%19
    e = (11*g + 29) % 30
    if e == 25 or e == 24:
        e += 1
 
    return (int((((e + d)*6+5)%177)/22) & 7)


if __name__ == "__main__":
    import sys

    tz_MX = pytz.timezone('America/Mexico_City')
    datetime_MX = datetime.now(tz_MX)
    #print("MX time: ", datetime_MX.strftime("%H:%M:%S"))

    sld = ""
    if datetime_MX.hour < 12:
        sld = "Hola buenos días"
    elif datetime_MX.hour < 18:
        sld = "Hola buenas tardes"
    else: 
        sld = "Hola buenas noches"

    if len(sys.argv) > 1:
        sld += ",  "
        sld += sys.argv[1]

    print(sld)
    print(f"Hoy es: {datetime_MX.strftime('%A')}, {datetime_MX.strftime('%B')} {datetime_MX.day}, {datetime_MX.year}")
    print(f"Son las {datetime_MX.strftime('%I:%M:%S %p')}")

    mp = moon_phase(datetime_MX.year, datetime_MX.month-1, datetime_MX.day)
    print(f"La luna está en {fases[mp]}")
    print(FraseDia())

