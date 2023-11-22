#Prac Test 1 
#Christopher Blignaut 
#BLGCHR003
#7 March 2022

i = eval(input("Enter the value of i:\n"))
j = eval(input("Enter the value of j:\n"))
k = eval(input("Enter the value of k:\n"))

if j==10:   #Data validation
    print("J cannot have the value 10.")
else:
    ans = int(round(k*(i-j)/(10-j),2))
    print("The answer is ",ans,".",sep="")