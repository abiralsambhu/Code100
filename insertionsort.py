##always maintaining a sorted sublist in the lower positions of the list. Each new item is then inserted back into the previous sorted sublist such that the sorted sublist is one item max than current


def insertionSort(lst):
    for index in range(1, len(lst)):
        currentvalue = lst[index] 
        currentposition = index
        while currentposition > 0 and lst[currentposition - 1] > currentvalue:
            lst[currentposition] = lst[currentposition - 1]
            currentposition -=1

        lst[currentposition] = currentvalue

######implementation ############################

lst = [33,54,23,13,45,78,88,56,90] #List defined for implementation
insertionSort(lst) #function call
print( "Sorted list is :",lst)


##OUTPUT####
#    Sorted list is : [13, 23, 33, 45, 54, 56, 78, 88, 90]
