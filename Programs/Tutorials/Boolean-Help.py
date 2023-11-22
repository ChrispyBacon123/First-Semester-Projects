from ast import And
from re import T


t1 = input("Do you have a sore throat (y/n)? ")
t2 = input("Do you have a dry cough (y/n)? ")
t3 = input("Do you have a headache (y?n)? ")

flag = False

if t1 == 'y' or t1=='Y':
    fT1=True
else:
    fT1=False
if t2 == 'y' or t2=='Y':
    fT2=True
else:
    fT2=False
if t3 == 'y'or t3 =='Y':
    fT3=True
else:
    fT3=False
    
if fT1 and fT2 and fT3:
    print("Status: Green")
    flag=True
if not fT1 and not fT2 and not fT3:
    print("Status: Red")
    flag = True
if flag==False:
    print("Status: Amber")