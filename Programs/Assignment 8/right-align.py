# Program that enters a list of names and right aligns them 
# Christopher Blignaut 
# BLGCHR003
# 18 April 

import array 
names = []
count = 0

# First value has to be entered to set a base value for the longest character 
names.append(input("Enter strings (end with DONE):\n"))


if names[0] != "DONE":
    # Entering the values for the array 
    while names[count] != "DONE":
        count = count + 1
        names.append(input())

        
    # Chopping off value for the DONE entry
    names.remove("DONE")
    count = count - 1 
    
    # Obtaining largest value for names 
    sortedNames = sorted(names, key=len)
    largest = sortedNames[count]

    
    # Printing output
    print("\nRight-aligned list:")
    
    for i in range(count+1):
        numSpace = len(largest)-len(names[i])
        print(" "*numSpace + names[i])
    
else:
    print("\nRight-aligned list:")