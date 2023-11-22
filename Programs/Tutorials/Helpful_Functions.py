# A bunch of helpful functions ready for copy and paste :)

# Binary Search
def binarySearch(values,query):
    #  The main binary search needs to be returned in a helper function to allow for recursion
    return binarySearch2(values,query,0,len(values)-1)
def binarySearch2(values,query,start,stop):
    """Binary search through values[start:stop+1] for query."""
    # check if list is empty
    if start > stop: # if it is empty, it means that the value was not in the list
        return -1
    # find midpoint
    middle = (start + stop) // 2
    # check if value is at midpoint
    if values[middle] == query:
        return middle
    # check if value is in second half
    if values[middle] < query:
    # recursively search second half
        return binarySearch2 (values, query, middle+1, stop)
    # assume value is in first half and recurse
    return binarySearch2 (values, query, start, middle-1)

# Selection Sorting
def selectionSorting(arr):
    """Sort an array from decending to ascending order"""
    for i in range(len(arr)-1):
        smolVal = i
        for j in range(i+1,len(arr)):
            if arr[smolVal] > arr[j]:
                newVal = j
                arr[i],arr[j] = arr[newVal],arr[smolVal]

# Merge Sorting 
def merge (list1,list2):
    """Merges the 2 sorted lists"""
    new_list = []
    while len(list1)>0 and len(list2)>0:
        if list1[0]<list2[0]:
            new_list.append(list1[0])
            del list1[0]
        else:
            new_list.append(list2[0])
            del list2[0]
    # The remainder of the larger list will still be sorted, 
    # so we can just add that onto the new list
    return new_list+list1+list2
def merge_sort(arr):
    """Sorting the arr using the merge sort algorithm"""
    if len(arr)>1:
        # Dividing the array into the small bits
        sortArr1 = merge_sort(arr[:len(arr)//2])
        sortArr2 = merge_sort(arr[len(arr)//2:])
        return merge(sortArr1,sortArr2)
    else:
        return arr
    
# Quick Sorting
def swap (values,first,second):
    """Swap the first and second values in a list"""
    values[first],values[second] = values[second],values[first]
def partition(values,start,stop):
    """Partition list in the place based on the pivot value"""
    pivot = values[stop]
    midpoint = start
    for i in range(start,stop):
        if values[i]<= pivot:
            swap (values,i,midpoint)
            midpoint += 1
    swap (values,midpoint,stop)
    return midpoint
def quick_sort(values,start,stop):
    """Sort the values from start to stop"""
    if stop>start:
        pivot = partition(values,start,stop)
        quick_sort(values, start,pivot-1)
        quick_sort(values,pivot+1,stop)
def quick_sort2(values):
    """Sorting the values"""
    quick_sort(values,0,len(values)-1)
    return values
