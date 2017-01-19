def quick_sort(given_list):
    if len(given_list) < 1:
        return given_list
    else:
        pivot_element = given_list[0] #here I am choosing the first element to be a pivot
        left = quick_sort([element for element in given_list[1:] if element < pivot_element]) # moving smaller to left
        right = quick_sort([element for element in given_list[1:] if element > pivot_element]) #moving greater to right
        return left + [pivot_element] + right


#usage
mylist=[8,5,9,4,3,7,2,12,10]
print (quick_sort(mylist))
