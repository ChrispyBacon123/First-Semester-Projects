# Program to determine if an inputted string is a palindrome using recursion
# Christopher Blignaut 
# BLGCHR003
# 23 April 


def check_pal(userString):
    """Funtion to determine if the parameter is a palindrome or not"""
    listWord = list(userString)
    
    # Base case
    if len(listWord) <= 1:    # A one character input will always be a palindrome
        return "Palindrome!"
    
    elif listWord[0] == listWord[(len(listWord)-1)]:
        listWord.__delitem__(0)
        listWord.__delitem__(len(listWord)-1)
        
        uString = str(listWord)
        uString = uString.replace("[","")
        uString = uString.replace("]","")
        uString = uString.replace(", ", "")
        uString = uString.replace("'","")
        
        return check_pal(uString)
    
    # Base case
    else:
        return "Not a palindrome!"
    
    
    
    
def palindrome(string, length):
    reverse = string[len(string)-1]

    if length == 1:
        if string[0] == reverse:
            return "Palindrome!"
        
        else:
           return "Not a palindrome!"
    else:
        #reading in the string backwards using recursion
        length -= 1
        reverse += string[length-1]
        return palindrome(string, length)


def main():
    userString = input("Enter a string:\n")
    print(check_pal(userString))  
    print(palindrome(userString, len(userString)))

if __name__ == '__main__':
   main()