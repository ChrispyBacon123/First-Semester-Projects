# Module to determine if a given pattern matches a given word.
# Christopher Blignaut 
# BLGCHR003
# 23 April 

def match(pattern,word):
    """determine if a given pattern matches a given word."""
    # Pattern has to be at least one character like the word
    if len(pattern) == 0 : 
        return False
    
    # Pattern and word have to be same length
    if len(pattern) != len(word): 
        return False
    
    # Base Case 1
    if len(pattern) == 1:
        if pattern[0] == word[0] or pattern[0] == "?": 
            return True
        
    # Base Case 2
    if pattern[0] != "?": 
        if pattern[0] != word[0]: 
            return False
        
    return match(pattern[1:], word[1:])    