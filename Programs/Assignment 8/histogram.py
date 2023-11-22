# Program to take in a list of marks and output a histogram displaying the marks
# Christopher Blignaut 
# BLGCHR003
# 18 April 

def print_histogram(marks):
    """Create and print out histogram"""
    
    markArrString = marks.split(" ")

    # Converting the list of strings into a list of integers
    markArr = []
    for i in range(len(markArrString)):
        markArr.append(int(markArrString[i]))


        
    markArr.sort(reverse = True)
    first = 0
    uSec = 0
    lSec = 0
    third = 0 
    fail = 0

    # Determining the spread of results
    for i in range(len(markArr)):
        if markArr[i] >= 75:
            first += 1
        elif markArr[i] >= 70 and markArr[i] < 75:
            uSec += 1
        elif markArr[i] >= 60 and markArr[i] < 70:
            lSec += 1
        elif markArr[i] >= 50 and markArr[i] < 60:
            third += 1
        else: 
            fail += 1 
            
    # Printing out graph
    print("1 |"+("X"*first))
    print("2+|"+("X"*uSec))
    print("2-|"+("X"*lSec))
    print("3 |"+("X"*third))
    print("F |"+("X"*fail))
    
    
def main():
    marks = input("Enter a space-separated list of marks:\n")
    print_histogram(marks)

if __name__ == '__main__':
   main()