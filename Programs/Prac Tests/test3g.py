# CSC1015F Test 3: Version G
# Given a string, find the first uppercase character.
# Christopher Blignaut
# BLGCHR003
# 9 May 2022

def find_uppercase(input_str, idx = 0):
    """Function to find the first uppercase character in a string using recursion"""
    
    # Base Case 
    if len(input_str) == idx:
        return -1
    
    # If the character is an uppercase character
    elif str(input_str[idx]).isupper():
        return str(input_str[idx])
    else:
        return find_uppercase(input_str,idx+1)
    

def main():
    input_string = input("Enter a string:\n")
    if input_string == '':
        print('No string supplied', end='.')
    else:
        print("The first uppercase character is:", find_uppercase(input_string, 0), end='.')

if __name__ == '__main__':
    main()
