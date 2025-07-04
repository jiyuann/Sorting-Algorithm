def bubblesort(array):
    """
    sorts the array of integers from smallest to biggest
    """
    #iterates the iteration 
    for i in range(len(array) - 1):
        swap = False
        #iterate from one element to another
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                swap = True
        if swap == False:
            return array
    return array
mylist = [1, 2, 3, 4]  
print(bubblesort(mylist))

#without a fucntion
i = 0
j = 0
while i < (len(mylist) -1):
    swap = False
    #iterate from one element to another
    while j < (len(mylist) - 1 - i):
        if mylist[j] > mylist[j + 1]:
            temp = mylist[j]
            mylist[j] = mylist[j + 1]
            mylist[j + 1] = temp
            swap = True
            j += 1
    i += 1
print(mylist)

mylist = [4, 2, 1, 3]  
print(bubblesort(mylist))
