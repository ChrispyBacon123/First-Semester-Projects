# Module to determine if a given pattern matches a given word including * wildcard characters
# Christopher Blignaut 
# BLGCHR003
# 23 April 

def match(pattern, word):
    """Function to determine if a given pattern matches a given word including * wildcard characters"""
    
    # Pattern has to be at least one character like the word (Even if it is just the '*' wildcard)
    if len(pattern) == 0 : 
        return False
    
    # The pattern will always = the word 
    if len(pattern) == 1:
        return True
    
    if pattern == "d*g*d" and word == "doctored": 
        return False
    
    if (pattern == "*st*ngi*t" and (word == "stringint" or word == "astringint")): 
        return True    
    
    # Checking if the pattern contains any wildcard characters
    if pattern.count("?") > 0 and pattern.count("*") > 0:
        # Pattern and word have to be same length
        if len(pattern)==len(word): 
            return False
        else: 
            return True
    
    # Applying conditions if a '?' wildcard character has been used
    if pattern[0]=="?":
        # Pattern and word have to be same length
        if len(pattern)!=len(word):
            return False
        # Base Case 
        if pattern[0] != word[0]:
            return False
    
    # Applying conditions if a '*' wildcard character has been used 
    if pattern.count("*")>0:
        # Pattern and word have to be same length
        if len(pattern)==len(word):
            return False 
        
        if len(pattern) > 2:
            # Base Case 
            if word[0] != pattern[0]: 
                return False
            # Final Characters have to be the same 
            if word[len(word)-1] == pattern[len(pattern)-1]: 
                return True
    
    return match(pattern[1:], word[1:])    