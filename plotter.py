"""
Data Plotter Test
Solution by Dr. Thiri The Wut yee
There are many possible solutions.
"""
import turtle

def check(a,b,c):
    """
    check whether input range is between -100 and 100
    the function should return value to decide input is valid or invalid 
    """
    result=""
    if not (-100<a<100):
        result=result+ (str(a)+" is out of range \n")
    if not (-100<b<100):
        result=result+ (str(b)+" is out of range \n")
    if not (-100<c<100):
        result=result+ (str(c)+" is out of range")
    if len(result)>0:
        return "Data is not valid \n"+result
    else:
        return ""

def plot(a,b,c):
    """
    draw X,Y axix first
    draw 3 points and connect them with lines
    """
    drawxy()
    dota(a)
    dotb(b)
    dotc(c)
    
def drawxy():
    """
    this function draws X,Y axis 
    """
    turtle.fd(300)
    turtle.home()
    turtle.setheading(90)
    turtle.fd(100)
    turtle.home()
    turtle.setheading(-90)
    turtle.fd(100)
    turtle.home()
    

def dota(a):
    turtle.pencolor("black")
    turtle.goto(100,a)
    if a>0:
        turtle.dot(20,"green")
    else:
        turtle.dot(30,"red")
        
def dotb(a):
    turtle.pencolor("black")
    turtle.goto(200,a)
    if a>0:
        turtle.dot(20,"green")
    else:
        turtle.dot(30,"red")
def dotc(a):
    turtle.pencolor("black")
    turtle.goto(300,a)
    if a>0:
        turtle.dot(20,"green")
    else:
        turtle.dot(30,"red")
     


#beginning of main()
#Step 1: User inputs    
print("The Data Plotter")
a,b,c=input("Give me 3 integer numbers separated by space").split()
a=int(a)
b=int(b)
c=int(c)
#Step 2: Check input out of range
result=check(a,b,c)

#Step 3: Draw points
if len(result)>0:
    print(result)
    exit
else:
    plot(a,b,c)
    
