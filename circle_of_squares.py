#import the turtle library
import turtle

#assign
my_turtle=turtle.Turtle()

# define a squar function which draws a square, and
# also shifts the angle after one square is drawn
def squar(len,ang,shift_angle):
  for i in range(0,4):
    my_turtle.forward(len)
    my_turtle.right(ang)
  my_turtle.right(shift_angle)
  
#call the square function
for i in range(0,36):
  squar(100,90,100)
  
  
