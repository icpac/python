
palabra = input("Capture la palabra: ")

if palabra[0] in "aeiou":
    pig = palabra + "way"
else:
    pig = palabra[1:]+palabra[0]+"ay"

print(pig)