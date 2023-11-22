def main():
    studs = {}
    again = ""
    while again.upper() != "N":
        studentNO = input('Enter a unique student number:')
        studentNO = studentNO.upper()
        name = input("Enter the student's name: ")
        studs[studentNO] = [name,[]]
        
        mark = input("Add a mark (N to finish marks): ")
        while mark.upper() != "N":
            studs[studentNO][1].append(eval(mark)) 
            mark = input("Add a mark (N to finish marks): ")
        
        again = input("Do you want to add another student (Y/N)? ")   
        
    for i in studs:
        print(i,":",studs[i])
main()