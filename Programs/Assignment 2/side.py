#A program to calculate the shorter size of a triangle
#Christopher Blignaut BLGCHR003
#1 March 2022

import math #Importing libraries

a = eval(input("Enter the length of side a:\n")) #Entering values
c = eval(input("Enter the length of side c:\n"))

if a>0 and c>0:
    b = math.sqrt(c**2-a**2) #Calculating the other side of the triangle
    print("The length of side b is",b, end=".")
else:
    print("Sorry, lengths must be positive numbers.")