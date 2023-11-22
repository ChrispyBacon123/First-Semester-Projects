# Module to create hollow boxes of stars
# Christopher Blignaut 
# BLGCHR003
# 31 March 

import math

# A method to print out a 5x5 square
def print_square():
    outp = "* * * * *\n"
    out = ""
    for i in range(3):
        outp = outp+"*"+(" "*7)+"*\n"
    return outp


# A method to print out a box with the given measurements
def print_rectangle(width, height):
    print (("* "*width))
    spaces = len(("* "*width))-3
    out = ""
    for i in range(height-2): #Range = height - 2 to account for the first and last row that are printed
        out = out+"*"+(" "*(spaces))+"*\n"
        
    print(out,end="")
    print (("* "*width))


# A method to return a string that is a box with the given measurements
def get_rectangle(width, height):
    out = ("* "*width)+"\n"
    spaces = len(out) - 3
    for i in range(height-2): # Range = height - 2 to account for the first and last row that are printed
     out = out+"*"+(" "*(spaces-1))+"*\n"
        
    out = out +("* "*width)
    return out

def main():
    output= get_rectangle(4,8)


if __name__=='__main__':
    main()