
import urllib.request

cualPal = input("Qué palabra quieres: ")

target_url = "https://www.thelatinlibrary.com/tacitus/tac.ann1.shtml"
for line in urllib.request.urlopen(target_url):
    #print(line.decode('utf-8'))
    linea = str(line.decode('utf-8'))
    if linea.find(cualPal) > 0:
        print(f"Existe {cualPal} !")