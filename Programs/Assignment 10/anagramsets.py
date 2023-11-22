# Program to accept the length of words and to write all anagrams of that length into a text file
# Christopher Blignaut 
# BLGCHR003
# 1 May

import anagramsearch

def split(word):
    """Function to split a word into a dictionary from the hint of question 1 ... 
    which I only read when I got to question 3 :("""
    letters = {}
    
    #Counting the number of each letter in the words
    for i in range(len(word)):
        if word[i] in letters:
            letters[word[i]] += 1        
        else: 
            letters[word[i]] = 1
            
    return letters

def get_anagrams(wordArr):
    """Function to sort through an array and return a list of anagrams found in the parameter list"""
    out = []
    message= []
    numbers = []
    
    for i in range(len(wordArr)):
        val = split(wordArr[i])
        for j in range(len(wordArr)):
            
            if wordArr[j] not in numbers:
                k = split(wordArr[j])
                
                # Using hint from question 1 :(
                if k == val:
                    out.append(wordArr[j])
                    numbers.append(wordArr[j])
                    
        # Making sure that a list of only the primary word is not returned     
        if len(out)>=2:
            message.append(sorted(out))            
        out = []
    message = sorted(message)
    return message


def main():
    print("***** Anagram Set Search *****")
    lenWord = int(input("Enter word length:"))
    print("Searching...")
    fileName = input("Enter file name:")
    
    # Reading words from the text file using the method from q1
    wordArr = anagramsearch.read_words(lenWord)
    # Retrieving the anagrams from the list of words 
    anagrams = get_anagrams(wordArr)
    
    # Writing to file
    print("Writing results...")
    try:
        file = open(fileName,'w')
    
        for i in range(len(anagrams)):
            print(anagrams[i],file=file)    
        file.close()
        
    except IOError:
        print("")
    
    print("done")
        
    
if __name__ == '__main__':
   main()
   
   
   #File extention to be used when testing
   #/Users/Chris/OneDrive - University of Cape Town/CSC1015/Programs/Assignment 10/