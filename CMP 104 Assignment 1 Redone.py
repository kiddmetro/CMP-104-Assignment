#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#IGWE CLINTON DONALD
#BHU/19/04/05/0003
#Level 100
#CMP 104


# In[11]:


#(1)
#Area of a Square
#Length of the sides is a
def Area_Square(a):
    Area = a**2
    return Area
    
a = int(input("Enter Number for a = "))

print(Area_Square(a))


# In[12]:


#(2)
#Area of Rectangle
#l is Length and b is Breadth
def Area_Rec(a,b):
    Area = l*b
    return Area

l = int(input(" Enter N5umber for l = "))
b = int(input(" Enter Number for b = "))

print(Area_Rec(a,b))


# In[13]:


#(3)
#Area of Triangle
# b is the base of triangle
# h is the height of triangle
def Area_Tri(a,b):
    Area = 1/2*b*h
    return Area
    
b = int(input(" Enter Number for b = "))
h = int(input(" Enter Number for h = "))

print(Area_Tri(a,b))


# In[18]:


#(4)
#Area of Trapezoid
#b1 & b2 are the bases of the Trapezoid
#h is the height of the Trapezoid 
def Area_Trape(b1,b2,h):
    Area = 1/2*(b1 + b2)*h
    return Area
    
b1 = int(input(" Enter Number for b1 = "))
b2 = int(input(" Enter Number for b2 = "))
h = int(input(" Enter Number for h = "))

print(Area_Trape(b1,b2,h))


# In[22]:


#(5)
#Area of a circle
#where Pi is 22/7
# r is the radius
def Area_circle(Pi,r):
    Area = Pi*r**2
    return Area

Pi = 22/7
r = int(input(" Enter Number for r = "))

print(Area_circle(Pi,r))


# In[24]:


#(6)
#Circumference of a circle
#where Pi is 22/7
# r is the radius
def Circum_circle(Pi,r):
    Circum = 2*Pi*r
    return Circum

Pi = 22/7
r =  int(input(" Enter Number for r = "))

print(Circum_circle(Pi,r))


# In[26]:


#(7)
#Surface Area of a Cube = S = 6a2
# a is the Length of the sides of a Cube
def SufArea_cube(a):
    surfaceArea = 6*a**2
    return surfaceArea

a = int(input(" Enter Number for a = "))

print(SufArea_cube(a))


# In[28]:


#(8)
#Curved surface area of a Cylinder = 2πrh
#where Pi is 22/7
# r is the radius
# h is the height
def SufArea_cylinder(Pi,r,h):
    surfaceArea = 2*Pi*r*h
    return surfaceArea

Pi = 22/7
r = int(input(" Enter Number for r = "))
h = int(input(" Enter Number for h = "))

print(SufArea_cylinder(Pi,r,h))


# In[29]:


#(9)
#Total surface area of a Cylinder 
#where Pi is 22/7
# r is the radius
# h is the height
def TotsurArea_cylinder(r,h):
    TotsurArea =  2 * math.pi * r * (r + h)
    return TotsurArea
import math

r = int(input("Enter Number for r = "))
h = int(input("Enter Number for h = "))

print(TotsurArea_cylinder(r,h))


# In[31]:


##### (10)
#Volume of a Cylinder 
#where Pi is 22/7
# r is the radius
# h is the height
def vol_cylinder(Pi,r,h):
    volcylinder = Pi*r*2*h
    return volcylinder
    
Pi = 22/7
r = int(input("Enter Number for r = "))
h = int(input("Enter Number for h = "))

print(vol_cylinder(Pi,r,h))


# In[32]:


#(11)
#Acceleration Formula (v-u)/t 
#v is final velocity 
# u is initial velocity
#t is time
def Acceleration(v,u,t):
    acceleration = (v-u)/t
    return acceleration

v = int(input("Enter Number for v = "))
u = int(input("Enter Number for u = "))
t = int(input("Enter Number for t = "))

print(Acceleration(v,u,t))


# In[33]:


#(12)
#density
#m is mass 
#v is volume
def density(m,v):
    density = m/v
    return density

m = int(input("Enter Number for m = "))
v = int(input("Enter Number for v = "))

print(density(m,v))


# In[34]:


#(13)
#pressure P=F/A 
#where F is force applied 
#A is total area of the object
def Pressure(F,A):
    pressure = F/A
    return pressure

F = int(input("Enter Number for F = "))
A = int(input("Enter Number for A = "))

print(Pressure(F,A))


# In[35]:


#(14)
#kinetic energy is E
#m is mass 
#v is volume
def Kinetic_Energy(m,v):
    kineticenergy =  1/2*m*v**2
    return kineticenergy
    
m = int(input("Enter Number for m = "))
v = int(input("Enter Number for v = "))

print( Kinetic_Energy(m,v))


# In[36]:


#(15)
#V is for voltage V = IR
#I is current and R is resistance in ohms
def voltage(I,R):
    voltage = I*R
    return voltage

I = int(input("Enter Number for I = "))
R = int(input("Enter Number for R = "))

print(voltage(I,R))


# In[ ]:




