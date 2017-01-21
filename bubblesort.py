
def bubbleSort(lst):
    currentindex =0
    endindex=len(lst) -1
    
    
    while currentindex< endindex:
        nextindex = currentindex + 1
        if lst[currentindex] > lst[nextindex]:
            lst[nextindex], lst[currentindex] = lst[currentindex], lst[nextindex] #swapping operation its fun with python
        
        if currentindex == endindex-1:
            currentindex = 0
            endindex = endindex-1          #Its Done because
                                           #final element gets sorted in above operation
            continue

            
        currentindex +=1



#implementation

lst=[88,74,56,34,89,67,56]
print lst
bubbleSort(lst)
print lst

#gives output as 
[88, 74, 56, 34, 89, 67, 56]
[34, 56, 56, 67, 74, 88, 89]

