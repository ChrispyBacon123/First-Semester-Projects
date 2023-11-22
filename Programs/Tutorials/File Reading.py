

def senenceSplit(text):
    text = str(text)
    text = text.replace('?',".").replace('!','.')
    new_text = text.split('.')
    return new_text

def main():
    try:
        file = open("chungus.txt","r")
        lines = file.readlines()
        file.close()
        new_lines = []
        for i in range(len(lines)-1):
            new_lines.append(senenceSplit(lines[i]))
            
        file = open("newChungus","w")
        file.writelines(new_lines)
        file.close()
        print("Have a nice day :)")
        
    except IOError:
        print('It dun f*cked up')    
    
main()