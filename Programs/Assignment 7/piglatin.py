# Functions to convert a sentence from pig latin into english and vise versa 
# Christopher Blignaut 
# BLGCHR003
# 10 April      
 
# Function to convert an english sentence into pig latin                       
def to_pig_latin(sentence):
    words = str(sentence).split(" ")
    out = ""

    for i in range(0,len(words)):
        noVowels = True
        word = words[i].lower()
        
        # Checking for vowels    
        if word[0] in "aeiou":
            word = word + "way"
            
        # Checking consonants
        else:  
            for letter in range(0,len(word)):
                
                if word[letter] in "aeiou":
                    mark = letter
                    word = word[mark:] + "a" + word[0:mark] + "ay"
                    noVowels = False
                    break 
               
            # In the case that there are no vowels in the word 
            if noVowels:
                word = word[1:] + "a" + word[0] + "ay"
                
        out = out + word +" "
    
    return out

# Function to convert a pig latin sentence into english
def to_english(sentence):
    words = sentence.split(" ")
    out = ""
    
    for word in words:
        
         # For words starting with vowels  
         # Use the phrase 'yaw' as is is the reverse of 'way' because we are looping from string from the end with slicing 
        if word[:len(word) - 4 : -1 ] == 'yaw':
            out = out + word[:len(word) - 3] + " "
        
        # For words starting with consonants    
        else: 
            noSuff = word[:len(word) - 2]          
            # Looking for the a which is just before the starting letters
            startWord = noSuff.split("a")[-1]      
            # Generating output
            out = out + startWord + noSuff[:len(noSuff) - (len(startWord)+1)] + " "
            
    return out
