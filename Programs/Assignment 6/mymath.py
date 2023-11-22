# Module to calculate the number of k-permutations of n items
# Christopher Blignaut 
# BLGCHR003
# 31 March 


# Function to  retrieve the number of items 
def get_integer(s):
    n = input ("Enter "+s+":\n")
    while not n.isdigit ():
        n = input ("Enter "+s+":\n")
    n = eval (n)   
    return n
 

# Function to calculate the number of permutations
def calc_factorial(n):
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    
    return nfactorial

print(get_integer())