# Module to determine if a given word is an anagram of any words found in the textfile EnglishWords.txt
# Christopher Blignaut 
# BLGCHR003
# 1 May

def read_words(lenWords):
    """Function to skip through the copywrite notice and read all the words into an array"""
    wordArr = []
    shortenedWordArr = []
    try:
        file = open('EnglishWords.txt','r')
        line = ""
        
        # Ignoring the refrencing at the top of the file 
        while(line != "START\n"):
            line = file.readline()
            
        # Reading rest of the words into an array
        wordArr = file.readlines()
        for i in range(len(wordArr)):
            word = str(wordArr[i].replace("\n",""))
            # Shortening the array to only words of the correct length
            if len(word) == lenWords or lenWords == 0:
                shortenedWordArr.append(word)
                
        file.close()
    except IOError:
        return "Sorry, could not find file 'EnglishWords.txt'."
        
    shortenedWordArr.sort()
    return shortenedWordArr
        
def anagram_list(word,wordArr):
    """Function to read the array containg the data from 
    the text file and output a list of words that are anagrams of the parameter word"""
    anagrams = []
    
    word = word.lower()
    check = word
    word = str(sorted(word))
    word = word.replace("[","")
    word = word.replace("]","")
    word = word.replace(", ", "")
    word = word.replace("'","")
    word = word.replace("\\","")
    
    for i in range(len(wordArr)):
        wordI = str(wordArr[i]).replace("\n","")
            # Anagrams will always be the same length
        if len(word) == len(wordI):
                
            # Filtering out if the original word that was entered if it is in the textfile
            if wordI != check:
            # Ordering all the string's characters alphabetically 
                wordI = str(sorted(wordI))
                wordI = wordI.replace("[","")
                wordI = wordI.replace("]","")
                wordI = wordI.replace(", ", "")
                wordI = wordI.replace("'","")
                wordI = wordI.replace("\\","")
                wordI = wordI.replace("\n","")
                if word == wordI:
                        word_to_append = wordArr[i].replace("\n","")
                        anagrams.append(word_to_append)
        
    if len(anagrams) == 0:
        return "Sorry, anagrams of '"+check+"' could not be found."
    else:    
        anagrams.sort()             
        return anagrams
    

def main():
    print("***** Anagram Finder *****")
    wordArr = read_words(0)
    if wordArr != "Sorry, could not find file 'EnglishWords.txt'.":
        word = input("Enter a word:\n")
        print(anagram_list(word,wordArr))
    else:
        print(wordArr)
    
    
if __name__ == '__main__':
   main()
   
   # File extention used for testing the program on this computer
   #'/Users/Chris/OneDrive - University of Cape Town/CSC1015/Programs/Assignment 10/