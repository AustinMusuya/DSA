numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubble_sort(array):
  for i in range(len(array) - 1):
    for j in range(i+1, len(array)):
      if array[i] > array[j]:
        temp = array[i]
        array[i] = array[j]
        array[j] = temp

  return array

def the_real_bubble_sort(array):
  size = len(array)
  for i in range(size - 1):
    swapped = False # Set a boolean flag to track swaps
    for j in  range((size - 1) - i): # Reduce the range after every outer loop iteration
      if array[j] > array[j+1]:
        # Swap adjacent Elements
        [array[j], array[j+1]] = [array[j+1], array[j]]
        swapped = True
    if not swapped: # Exit if no swaps (already sorted)
      break

  return array

print(f'unsorted array : {numbers}')

the_real_bubble_sort(numbers)

print(f'sorted array : {numbers}')
