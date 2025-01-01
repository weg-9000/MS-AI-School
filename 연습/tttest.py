from turtle import *
import random
shape("turtle")
pensize(3)
for i in range(10):    
       r = random.random()
       g = random.random()
       b = random.random()


       x = random.randint(-300,300)
       y = random.randint(-300,300)
       length = random.randint(10,300)

       penup()
       goto(x,y)
       pendown()
       color(r,g,b)
       begin_fill()
       for j in range(5):
            forward(length)
            right(90)
            end_fill()


