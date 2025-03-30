numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[-1] # Use simpler indexing
    left = []
    right = []
    
    # Simplified partitioning by building new lists
    for x in array[:-1]:
        if x <= pivot:
            left.append(x) 
        else:
            right.append(x)
            
    return quick_sort(left) + [pivot] + quick_sort(right)
