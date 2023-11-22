# Prac Test 2
# Christopher Blignaut 
# BLGCHR003
# 4 April 2022


inp = input("Enter a value (or 'DONE'):\n")
numPairs = 0
prevInp = inp

while inp != "DONE":
    inp = input("Enter a value (or 'DONE'):\n")
    
    if prevInp.isdigit() and inp.isdigit():
        numPairs = numPairs + 1
        
    prevInp = inp
    
print("Number of pairs of adjacent numbers:",numPairs)