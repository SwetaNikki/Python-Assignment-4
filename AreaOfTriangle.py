"""
1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
formula.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the parent
class and function to calculate the area should be defined in subclass.

"""
import math

class TakingInput:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
a = int(input("Enter a value : "))
b = int(input("Enter b value : "))
c = int(input("Enter c value : "))
        
class AreaOfTriangle(TakingInput):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)
      
    def area(self):
        s=(a+b+c)/2
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        return area
        
        
ob = AreaOfTriangle(a,b,c)
print("Area of Triangle : {}".format(ob.area()))

