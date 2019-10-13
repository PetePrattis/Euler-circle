# ! /usr/bin/env python
# -*- coding: utf-8 -*-

#Author Παναγιώτης Πράττης/Panagiotis Prattis

'''
The task accepts an input as a number, for n odd number it shows that there is an Euler circle for n = 5,7,9,11 
it shows the graph and the process of joining all peaks without repeating the links
'''

import turtle


#A Procedue to draw any regular polygon with 3 or more sides.
def drawPolygon(numberOfsides):
    exteriorAngle=360/numberOfsides
    length=600/numberOfsides
    points = [None] * numberOfsides
    myPen.penup()
    myPen.goto(-length/2,-length/2)
    myPen.pendown()
    for i in range(0,numberOfsides):
        points[i] = myPen.position()
        myPen.penup()
        myPen.shape("arrow")
        myPen.forward(length)
        myPen.left(exteriorAngle)
        myPen.shape("circle")
        myPen.stamp()
    if (numberOfsides == 5):
        circuit_five(points)
    elif (numberOfsides == 7):
        circuit_seven(points)
    elif (numberOfsides == 9):
        circuit_nine(points)
    elif (numberOfsides == 11):
        circuit_eleven(points)
    else:
        print("Too big a graph to draw.")


#A Procedue connect all points to each other visiting them once for a 5-polygon.
def circuit_five(p):
    index = 0
    step = 1
    for i in range (0, 5):
        myPen.pendown()
        if(index+step == 5):
            index = 0
        else:
            index = index + step
        myPen.goto(p[index])
        
    index = 0
    step = 2
    for i in range (0, 5):
        myPen.pendown()
        if (index + step == 5):
            index = 0
        elif (index + step > 5):
            index = 1
        else:
            index = index + step
        myPen.goto(p[index])

#A Procedue connect all points to each other visiting them once for a 7-polygon.
def circuit_seven(p):
    index = 0
    step = 2
    for i in range (0, 7):
        myPen.pendown()
        if(index+step == 7):
            index = 0
        elif(index+step == 8):
            index = 1
        else:
            index = index + step
        myPen.goto(p[index])
    index = 0
    step = 3
    for i in range (0, 7):
        myPen.pendown()
        if(index+step == 7):
            index = 0
        elif(index+step == 8):
            index = 1
        elif(index+step == 9):
            index = 2
        else:
            index = index + step
        myPen.goto(p[index])
    index = 0
    step = 1
    for i in range (0, 7):
        myPen.pendown()
        if(index+step == 7):
            index = 0
        else:
            index = index + step
        myPen.goto(p[index])
        
#A Procedue connect all points to each other visiting them once for a 9-polygon.
def circuit_nine(p):
    index = 0
    step = 2
    for i in range (0, 9):
        myPen.pendown()
        if(index+step == 9):
            index = 0
        elif(index+step == 10):
            index = 1
        else:
            index = index + step
        myPen.goto(p[index])
    index = 0
    step = 3
    for i in range (0, 3):
        myPen.pendown()
        if(index+step == 9):
            index = 0
        else:
            index = index + step
        myPen.goto(p[index])
    index = 0
    step = 4
    for i in range (0, 9):
        myPen.pendown()
        if(index+step == 9):
            index = 0
        elif(index+step == 10):
            index = 1
        elif(index+step == 11):
            index = 2
        elif(index+step == 12):
            index = 3
        else:
            index = index + step
        myPen.goto(p[index])
    index = 1
    myPen.goto(p[index])
    step = 3
    for i in range (0, 3):
        myPen.pendown()
        if(index+step == 10):
            index = 1
        else:
            index = index + step
        myPen.goto(p[index])
    index = 2
    myPen.goto(p[index])
    step = 3
    for i in range (0, 3):
        myPen.pendown()
        if(index+step == 11):
            index = 2
        else:
            index = index + step
        myPen.goto(p[index])
    index = 2
    myPen.goto(p[index])
    step = 1
    for i in range (0, 7):
        myPen.pendown()
        if(index+step == 9):
            index = 0
        else:
            index = index + step
        myPen.goto(p[index])

#A Procedue connect all points to each other visiting them once for a 11-polygon.
def circuit_eleven(p):
    index = 0
    step = 2
    for i in range (0, 11):
        myPen.pendown()
        if(index+step == 11):
            index = 0
        elif(index+step == 12):
            index = 1
        else:
            index = index + step
        myPen.goto(p[index])
    index = 0
    step = 3
    for i in range (0, 11):
        myPen.pendown()
        if(index+step == 11):
            index = 0
        elif(index+step == 12):
            index = 1
        elif(index+step == 13):
            index = 2
        else:
            index = index + step
        myPen.goto(p[index])
    index = 0
    step = 4
    for i in range (0, 11):
        myPen.pendown()
        if(index+step == 11):
            index = 0
        elif(index+step == 12):
            index = 1
        elif(index+step == 13):
            index = 2
        elif(index+step == 14):
            index = 3
        else:
            index = index + step
        myPen.goto(p[index])
    index = 0
    step = 5
    for i in range (0, 11):
        myPen.pendown()
        if(index+step == 11):
            index = 0
        elif(index+step == 12):
            index = 1
        elif(index+step == 13):
            index = 2
        elif(index+step == 14):
            index = 3
        elif(index+step == 15):
            index = 4
        else:
            index = index + step
        myPen.goto(p[index])
    index = 0
    step = 1
    for i in range (0, 11):
        myPen.pendown()
        if(index+step == 11):
            index = 0
        else:
            index = index + step
        myPen.goto(p[index])

#Main
sides = int(input("Give a number n > 3 or -1 to terminate:"))
myPen = turtle.Turtle()
while sides != -1:
    myPen.clear()
    myPen.reset()
    myPen.shape("arrow")
    myPen.color("red")
    if(sides <= 3 or sides % 2 == 0):
        print("An Euler circle exists only in graphs whose nodes have an  even degree")
        print("In a complete graph, only if there is an odd number of nodes there is a Euler circle.")
    else:
        drawPolygon(sides)
    sides = int(input("Give a number n > 3 or -1 to terminate:"))
    
