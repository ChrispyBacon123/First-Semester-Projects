#A program to calculate PI and then work out the area of a circle
#Christopher Blignaut BLGCHR003
#28 February 2022

import math #Importing libraries

pi=2*(2/math.sqrt(2))*(2/(math.sqrt(2+math.sqrt(2))))*(2/(math.sqrt(2+math.sqrt(2+math.sqrt(2)))))
print("Approximation of pi:", round(pi,4))
rad = eval(input("Enter the radius:\n"))
area = pi*(rad**2)
print ("Area:", round(area,4))