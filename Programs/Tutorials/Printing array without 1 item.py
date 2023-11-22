def Enigma(list, item):
    temp=[]
    for i in list:
        if i != item:
            temp.append(i)
    return temp

def main():
    list1=[2,4,6,6,8,10]
    list2 = ["Skipper","Kowalski","Ricko","Private","KingJulain"]
    list3 = [[1,2],[3,4],[5,6]]
    print (Enigma(list2,"Private"))
    print (Enigma(list3,[1,6]))
    
main()