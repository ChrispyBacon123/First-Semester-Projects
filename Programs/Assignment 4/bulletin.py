# Program to simulate an old Bulletin Board System
# Christopher Blignaut 
# BLGCHR003
# 11 March 

out = False
message = "no message yet" # Making sure program doesn't crash if user has not entered a message yet
while not out:
    option = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")  
    
    # Exit
    if option == "X" or option == "x":      
        out = True
    
    # Enter a message    
    if option == "E" or option == "e":                     
        message = input("Enter the message:\n")
     
     
    # View message   
    if option == "V" or option == "v":
        print("The message is:",message,"")
     
    # List files   
    if option == "L" or option == "l":
        print("List of files: 42.txt, 1015.txt")
    
    # Display file    
    if option == "D" or option == "d":
        fileName = input("Enter the filename:\n")
        if fileName == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        if fileName == "42.txt":
            print("The meaning of life is blah blah blah ...")
        if fileName !="42.txt" and fileName !="1015.txt":
            print("File not found")

print("Goodbye!")