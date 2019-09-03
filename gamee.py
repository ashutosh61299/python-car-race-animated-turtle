# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 04:00:05 2018

@author: ASHUTOSH
"""

import turtle
s=turtle.Screen()
b=turtle.Canvas()
a=turtle.Turtle()
a1=turtle.Turtle()
a4=turtle.Turtle()
a6=turtle.Turtle()
a7=turtle.Turtle()
a.hideturtle()

img1=r"END.gif"
img3=r"car1.gif"
img4=r"car2.gif"
s.addshape(img1)
s.addshape(img3)
s.addshape(img4)
a4.shape(img1)



s.setup (width=1366, height=748, startx=0, starty=0)
class bg():
   
    
    def bg1(self):
#        green part
        a4.speed(0)
        a.speed(0)
        a.penup()
        a.lt(180)
        a.fd(300)
        a.pd()
        a.fillcolor('green')
        a.begin_fill()
        a.pd()
        a.rt(90)
        a.fd(374)
        a.lt(90)
        a.fd(383)
        a.lt(90)
        a.fd(1366)
        a.lt(90)
        a.fd(374)
        a.lt(90)
        a.fd(374)
        a.end_fill()
        
#        FLAG
        
        a4.pu()
        a4.lt(90)
        a4.fd(300)
        
#        ROAD STONE
        
                
    def bg2(self):
        a1.speed(0)
        a1.penup()
        
        a1.fd(300)
        a1.pd()
        a1.fillcolor('green')
        a1.begin_fill()
        a1.rt(90)
        a1.pd()
        a1.fd(374)
        a1.lt(90)
        a1.fd(383)
        a1.lt(90)
        a1.fd(1366)
        a1.lt(90)
        a1.fd(374)
        a1.lt(90)
        a1.fd(374)
        a1.end_fill()
    
    def eein(self):
        a6.forward(3)
        
        
                
    def car1(self):
        
        a7.penup()
        a7.speed(2)
        
        a7.shape(img4)
        a6.penup()
        a6.shape(img3)
        a6.speed(1)         
        ei=-360
        ee=-360
        while(ei<300) and (ee<300):
            a6.setposition(-150,ee)
            a7.setposition(150,ei)
            ei=ei+0.75
            ee=ee+1
        
                
                
            
            
obj=bg()
obj.bg1()
obj.bg2()
obj.car1()
a6.write("WINNNER!!!")
s.exitonclick()
turtle.done()