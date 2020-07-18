import turtle

my_turtle=turtle.Turtle()

import turtle


my_turtle = turtle.Turtle()

def squar(len,ang,shift_angle):
  for i in range(0,4):
    my_turtle.forward(len)
    my_turtle.right(ang)
  my_turtle.right(shift_angle)
  
for i in range(0,36):
  squar(100,90,100)
  
  