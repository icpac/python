
__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

#Dibujar una función, por el momento vamos a dibujar los ejer coordenados.
#para usar las librerias

import pygame
import sys

#iniciamos la libreria
pygame.init()
#define la pantalla
pantalla = pygame.display.set_mode([640, 480])
#Llena la pantalla de un color
pantalla.fill([255, 255, 255])

#dibujamos los ejes coordenados
#eje x
pygame.draw.line(pantalla, [0,0,0], (0, 240), (640, 240), 1)
#eje y
pygame.draw.line(pantalla, [0,0,0], (320, 0), (320, 480), 1)

#graficar la función f(x) = x ** 2
for x in range(1, 640):
    #se corrige el movimiento del origen
    nx = x - 320
    #se mueve la función hacia la izquierda, y hacia abajo 
    ny = (nx + 52) ** 2 - 450 

    #se corrige el origen, y se contrae la gráfica
    y = 240 - (1/52 * ny)
    pygame.draw.rect(pantalla, [0,0,0], [x, y, 1, 1], 1)

pygame.display.flip()

#Eventos, el evento de salida
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

