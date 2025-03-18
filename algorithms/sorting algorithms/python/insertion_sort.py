numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
size = len(numbers)

def insertion_sort(array):
    for i in range(1,size):
        key = array[i]
        j = i - 1

        while j>=0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        
        array[j+1] = key
    
    return array

print(insertion_sort(numbers))