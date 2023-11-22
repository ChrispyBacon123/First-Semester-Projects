# Program to print out every 7th number after the user's entered number in a collumn
# Christopher Blignaut 
# BLGCHR003
# 9 March 2022

num = eval(input("Enter a number:\n"))
out = 0
if num < -6 or num >2:
    print("Number outside of specific range")
else:
    for out in range(num, num+41,7):
        
        if out >= 0 and out <= 9:
            print("",out)
        else:
            print(out)
        out = out+7