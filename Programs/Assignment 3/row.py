# Program to print out a row of 7 numbers from a given starting value
# Christopher Blignaut 
# BLGCHR003
# 9 March 2022


num = eval(input("Enter the start number:\n"))
if num < -6 or num >93:
    print("Number outside of specific range")
else:
    for i in range(num, num+7):
        if num>=0 and num<=9:
           print("",num,end=" ")
        else:
            print (num, end=" ")
        num+=1