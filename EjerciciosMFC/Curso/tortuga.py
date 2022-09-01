from turtle import *

#forward(100)
shape("turtle")

#puntos de un triángulo
long = 80

#reset()
#goto(0, 0)
penup()
goto(0, -long)
pendown()
dot(5)

#reset()
#goto(0, 0)
penup()
goto(-long*((3**(1/2))/2), long/2)
pendown()
dot(5)

#reset()
#goto(0, 0)
penup()
goto(long*((3**(1/2))/2), long/2)
pendown()
dot(5)

done()
