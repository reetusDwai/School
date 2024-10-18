# Complete the comments below
# Name: Kalem Smith
# Assignment: Lab 1, Exercise 3: polygons.py
# Date: 9/2/24
# List any issues you had with this lab
import turtle

turtle.setup(400, 400)
window = turtle.Screen()
window.title('Lab 1: Spiral')

t = turtle.Turtle()

angle = int(input("Enter angle: "))
size = 20

for i in range(128):
    t.forward(size)
    t.right(angle)
    size += 2
    
turtle.done()
