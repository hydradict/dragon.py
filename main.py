# dragon.py

p = 0



import turtle
t=turtle.Turtle()
t.color("black", "yellow")
t.begin_fill()
t.right(90)
t.forward(100)
t.left(90)
t.forward(250)
t.left(90)
t.forward(100)
t.left(90)
t.forward(300)
t.end_fill()

#Head
t.begin_fill()
t.color("black", "purple")
while p<4:
    p = p+1
    t.right(90)
    t.forward(75)
    t.color("black", "red")
t.end_fill()

#Sunglasses
t.begin_fill
t.backward(15)
t.right(90)
t.penup()
t.forward(50)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.right(90)
t.forward(60)
t.right(90)
t.forward(10)
t.right(90)
t.forward(15)
t.left(90)
t.forward(15)
t.right(90)
t.forward(25)
t.right(90)
t.forward(15)
t.left(90)
t.forward(10)
t.left(90)
t.forward(15)
t.right(90)
t.forward(25)
t.right(90)
t.forward(25)
t.right(90)
t.forward(75)
t.end_fill()

#Right horn
t.left(90)
t.forward(25)
t.color("black", "orange")
t.begin_fill()
t.right(35)
t.forward(20)
t.left(165)
t.forward(25)
t.end_fill()

#left horn
t.right(40)
t.forward(65)
t.color("black", "orange")
t.begin_fill()
t.right(35)
t.forward(20)
t.right(165)
t.forward(35)
t.end_fill()
t.left(20)
t.forward(60)

t.right(90)
t.foward(70)
