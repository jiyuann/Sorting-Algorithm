def insertionsort(mylist):
    """
    sort the list from smallest to biggest
    """
    i = 1
    for i in range(1, len(mylist)):
        target = mylist[i]
        j = i - 1
        swapped = False
        if swapped == False and mylist[j] < target:
            while j > -1 and mylist[j] > target:
                mylist[j+1] = mylist[j]
                j -= 1
                swapped = True
            mylist[j] = target
    return mylist

mylist = [2, 4, 3, 1]
print(insertionsort(mylist))