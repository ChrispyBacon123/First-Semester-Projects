# Program to draw a text based graph of a mathematical function
# Christopher Blignaut 
# BLGCHR003
# 23 March 

import math

#Getting input from user
fOfX = input("Enter a function f(x):\n")

#Used to make sure a | is not printed with the origin
originCheck = False

#Looping through every value it could be
for y in range (10, -11, -1):
    for x in range (-10, 11):
        func = round(eval(fOfX))
        
        #Used to add the plus at the origin of the graph 
        if x == 0 and y == 0 and y != func:
            print ("+", end="")
            originCheck = True
        
        #Printing Value
        if y == func:
            print ("o", end="") 
            xCheck = True
       
        #Drawing the rest of the graph
        elif x == 0 and y != func and not originCheck and not xCheck:
            print ("|", end="")
        elif y == 0 and y != func and x<10:
            print ("-", end="")
        else:
            print (" ", end="")

        originCheck = False
        xCheck = False

    #Used to go to next line (y-value) of graph
    print("")
    
#This was not fun :(