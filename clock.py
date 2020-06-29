"""
Data Plotter Test
Solution by Dr. Thiri The Wut yee
There are many possible solutions.
"""

import datetime
from turtle import * 

class clockface:
    def __init__(self,r,h,hl,ml,sl,c):
        self.r=r        #radius of clock face
        self.h=h        #length of number hands
        self.hl=hl      #lendth of hour hand 
        self.ml=ml      #lendth of minute hand
        self.sl=sl      #lendth of second hand
        self.c=c        #size of center point

    def draw(self):
        speed(100)
        penup()
        goto(0,-110)
        pendown()
        circle(self.r)
        for i in range(0,13):
            setheading((360/12)*i)
            penup()
            fd(self.r - self.h)
            pendown()
            fd(self.h)
            penup()
            home()
        dot(self.c,"red")
        hideturtle()

def main():
    c=clockface(110,10,30,40,50,15)
    c.draw()

#profiling start 
a = datetime.datetime.now()
main()
b = datetime.datetime.now()
             
print("Runtime ={}".format(b-a))
