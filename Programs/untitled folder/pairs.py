# Program to count the number of pairs of consecutive characters in a string
# Christopher Blignaut 
# BLGCHR003
# 23 April 

def num_Of_Pairs(message,index,count):
    """Function to determine the number of times two consecutive characters are placed together"""
    
    # Base Case 
    if index == len(message)-1:
        return count 

    if message[index] == message[index+1]:
        count += 1
        # Avoiding a string index out of range error
        if len(message[index:]) > 2:
            return num_Of_Pairs(message,index+2,count)
        else:
            return num_Of_Pairs(message,index+1,count)
    else:
        return num_Of_Pairs(message,index+1,count) 

def main():
    message = input("Enter a message:\n")
    print("Number of pairs:",num_Of_Pairs(message,0,0))
    
if __name__ == '__main__':
   main()