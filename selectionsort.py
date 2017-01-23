def selectionSort(lst):
   for selectedLocation in range(len(lst)-1,0,-1):
       maxPosition=0
       for currentindex in range(1,selectedLocation+1): #since range(0,4) is exclusive to 4
           if lst[currentindex]>lst[maxPosition]:
               maxPosition = currentindex

  
       lst[selectedLocation], lst[maxPosition] = lst[maxPosition],lst[selectedLocation] ##swapping a,b = b,a swaps a to b and b to a
      
##implementation
lst = []
print ("input array size")
i = int(input())
for a in range(0,i):
    ele= int(input(print("Enter element {0} ".format(a+1))))
    lst.append(ele)

selectionSort(lst)
print(lst)
