# Program to determine if the co-ordinates entered are valid
# Christopher Blignaut 
# BLGCHR003
# 9 March 2022

latDeg = eval(input("Enter first number:"))
latMin = eval(input("\nEnter second number:"))
latSec = eval(input("\nEnter third number:"))
lonDeg = eval(input("\nEnter fourth number:"))
lonMin = eval(input("\nEnter fifth number:"))
lonSec = eval(input("\nEnter sixth number:"))
flag = False

if latSec <=60 and latMin <=60 and lonMin <=60 and lonSec <=60 and latSec >=0 and latMin >=0 and lonMin >=0 and lonSec >=0:
    if latDeg >=-90 and latDeg <=90 and lonDeg >=-180 and lonDeg <=180:
        flag = True
    
if flag:
    print("\nWOW! Looks like geographic coordinates!")
else:
    print("\nHmmm ... looks like 6 random numbers.")

