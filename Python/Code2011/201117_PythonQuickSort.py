array = [5,7,9,0,3,1,6,2,4,8]
def quickSort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    return quickSort([x for x in tail if x < pivot]) + [pivot] + quickSort([x for x in tail if x > pivot])
print(quickSort(array))