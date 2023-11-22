# Program to determine if a prime number from a range of numbers is a palindrome using recursion
# Christopher Blignaut 
# BLGCHR003
# 23 April 

import palindrome
import sys
import math
sys.setrecursionlimit(30000)


def is_prime(num,count):
    """Funtion to determine if the number entered is a prime number"""
    
    # Any number smaller than or equal to 1 is not a prime
    if num <= 1:
        return False 

    else:
        if count <= math.sqrt(num):
            
                #Base Case
                if num == 2: 
                    return False
                elif (num % count) == 0:
                    return False
                # Recursion
                else:
                    return is_prime(num,count+1)
        return True

def palindrome_prime(n,m):
    """Function to print out all the palindrom prime numbers within the range of n to m"""
    # Base Case
    if n == m+1:
        return ""
    
    if is_prime(n,2) and palindrome.palindrome(str(n),len(str(n))) == "Palindrome!":     # Using method from question 2
            print(n)
            return palindrome_prime(n+1,m)
    else:
        return palindrome_prime(n+1,m)
    
def main():
    start = int(input("Enter the starting point N:\n"))
    end = int(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    palindrome_prime(start,end)
    
if __name__ == '__main__':
   main()