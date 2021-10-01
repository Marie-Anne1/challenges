print("*******************")
print("Challenges 060")
import turtle

for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
    
turtle.exitonclick()
print()

print("*******************")
print("Challenges 061")
import turtle

for i in range(0, 3):
    turtle.foward(100)
    turtle.left(120)
    
turtle.exitonclick()
print()

print("*******************")
print("Challenges 062")
import turtle

for i in range(0, 360):
    turtle.forward(1)
    turtle.right(1)
    
turtle.exitonclick()
print()

print("******************")
print("Challenges 063")
import turtle

turtle.color("black","red")
turtle.begin_fill()
for i in range (0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("black","yellow")
turtle.begin_fill()
for i in range (0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("black","green")
turtle.begin_fill()
for i in range (0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.end_fill()

turtle.exitonclick()
print()

print("*******************")
print("Challenges 064")
import turtle

for i in range (0,5):
    turtle.forward(100)
    turtle.right(144)

turtle.exitonclick()
print()

print("*******************")
print("Challenges 065")
import turtle

turtle.left (90)
turtle.forward (100)
turtle.right (90)
turtle.penup () 
turtle.forward (50)
turtle.pendown ()
turtle. forward (75)
turtle.right (90)
turtle.forward (50)
turtle.right (90)
turtle.forward (75)
turtle.left (90)
turtle.forward (50)
turtle.left (90)
turtle.forward (75)
turtle.penup ()
turtle.forward (50) 
turtle.pendown ()
turtle.forward (75)
turtle.left (90)
turtle.forward (50)
turtle.left (90)
turtle.forward (45)
turtle.left (180)
turtle.forward (45)
turtle.left (90)
turtle.forward (50)
turtle.left (90)
turtle.forward (75)

turtle.hideturtle()

turtle.exitonclick()
print()

print("*******************")
print("Challenges 066")
import turtle
import random

turtle.pensize(3)

for i in range (0,8):
    turtle.color(random.choice(["red","blue","yellow","green","pink","orange"]))
    turtle.forward(50)
    turtle.right(45)
    
turtle.exitonclick()
print()

print("*******************")
print("Challenges 067")
import turtle
import random

for x in range(0,10):
    for i in range (0,8):
        turtle.forward(50)
        turtle.right(45)
    turtle.right(36)
    
turtle.hideturtle()

turtle.exitonclick()
print()

print("*******************")
print("Challenges 068")
import turtle
import random

lines = random.randint(5,20)

for x in range(0,lines):
    length = random.randint(25,100)
    rotate = random.randint(1,365)
    turtle.forward(length)
    turtle.right(rotate)

turtle.exitonclick()
print()