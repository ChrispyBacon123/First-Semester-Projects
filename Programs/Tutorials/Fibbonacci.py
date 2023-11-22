from cgi import print_environ_usage
from multiprocessing.dummy import current_process


rab = int(input("EnHow many rabbits do you want"))

current=2
previous=1
gen=1
add=0

while current<=rab:
    gen+=1
    add=previous
    previous=current
    current=current+add
    
print ("You will reach that in ",gen," Generations.",end="")
