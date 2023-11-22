def fibonacci_rec(n):
    print("Calculating F","(",n,")",sep="",end=", ")
    
    if n==0:
        print("return 0")
        return 0
    elif n==1:
        print("return 1")
        return 1
    
    else:
        print ("Calculate: F(",n-1,")+F(",n-2,")",sep ='' )
        return fibonacci_rec(n-1)+fibonacci_rec(n-2)
    
def sortArr(arr,leng,index = 0):
    if leng == index:
        return -1
    else:
        if z != index:
            arr[z],arr[index] = arr[index] , arr[z]
            sortArr(arr,leng,index+1)
    
print(fibonacci_rec(4))
        #  
        #  
        #  if n != index 
        #   if arr[index]>arr[n]
        #    temp = arr[index]
        #    arr[index] = arr[n]
        #    arr[n] = temp
        #    return RSS(arr,n,index+1)
        #  
        #  
        #  
        #  
        #  
        #  
        #  
        #  
        #  
        #  
        #  
        #  
        #  
        #  
        #  
        #  
        #  