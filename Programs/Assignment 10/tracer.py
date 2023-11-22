# Program to assist in the debugging of other programs 
# Christopher Blignaut 
# BLGCHR003
# 1 May

def debug(declaration):
    """Function to generate a docstring to be added into the file"""
    # Finding the name of the function
    declaration = declaration.split()
    # Fixing to stop the first parameter from being mistaken as part of the function name
    funcName = declaration[1]
    if str(funcName).__contains__("("):
        funcNameArr = str(funcName).split("(")
        funcName = funcNameArr[0]
        
    # Adding text to the code file 
    return '    """DEBUG""";print(\'' + str(funcName) + '\')\n' 

def main():
    print("***** Program Trace Utility *****")
    file = input("Enter the name of the program file: ")
    f = open(file,"r")
    lines = f.readlines()
    f.close()
    
    # Checking if file has already been debugged
    if lines[0] != '"""DEBUG"""\n':
        print("Inserting...", end="")
        lines.insert(0,'"""DEBUG"""\n')
        i = 0
        count = len(lines)
        
        # Finding method declaration and adding the debug docscript 
        while i < count:
            if lines[i][0:3] == "def":
                lines.insert(i+1,debug(lines[i]))
                count += 1
                
            i+=1
        print("Done")
        
    else: 
        print("Program contains trace statements")
        print("Removing...",end="")
        del lines[0]
        i = 0
        count = len(lines)
        
        # Finding traces of DEBUG docscript and removing it 
        while i < count:
            if lines[i][0:3] == "def":        
                del lines[i+1]
                count -= 1
                
            i+=1
        print("Done")
            
    f = open(file,'w')
    for i in lines:
        print(i, file=f,end="")
    f.close    
    
if __name__ == '__main__':
   main()
   
#/Users/Chris/OneDrive - University of Cape Town/CSC1015/Programs/Assignment 10/File to be zipped/rfunction.py