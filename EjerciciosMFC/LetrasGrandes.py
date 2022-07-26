

class Objeto():
    def __init__(this, que):
        this.Cual = que

    def __str__(this) -> str:
        return "esto es lo que imprime " + this.Cual

    def Metodo(this):
        pass

obj = Objeto("No se")

print(obj)
print(obj.Cual)


import Saludo

Saludo.FraseDia()

