numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def selectionSort(array):
    if len(array) == 0:
        return None
    size = len(array)
    for i in range(size):
        min = i
        for j in range(i+1, size):
            if array[j] < array[min]:
                min = j
                
        # swap the values min and first index
        (array[i], array[min]) = (array[min], array[i]) 
    return array

print(selectionSort(numbers))
