# A Game Of Wordle
# Christopher Blignaut 
# 22 March 2022

ans ="TRADE"
word = input("What is your guess?")
word = word.upper()
print("["+word+"]")

out = "["

for i in range(len(word)):
    if word[i] == ans[i]:
        out = out+"*"
    elif word[i] in ans:
        out = out+"+"
    else:
        out = out+"-"
        
out = out+"]"
print(out)