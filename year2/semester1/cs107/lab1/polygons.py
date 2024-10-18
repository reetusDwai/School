# Complete the comments below
# Name: Kalem Smith
# Assignment: Lab 1, Exercise 3: polygons.py
# Date: 9/2/24
# List any issues you had with this lab
import turtle

turtle.setup(1000, 600)
window = turtle.Screen()
window.title('Lab 1: Polygons')

t = turtle.Turtle()

t.penup()
t.setposition(-450, 0)
t.pendown()

side_length = int(input("Enter an integer side length: "))

for i in range(3, 8):
    angle = 360 / i
    for j in range(i):
        t.forward(side_length)
        t.left(angle)
    t.forward(side_length * 3)

turtle.done()
