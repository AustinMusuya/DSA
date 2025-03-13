numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubbleSort(array):
  for i in range(len(array) - 1):
    for j in range(i+1, len(array)):
      if array[i] > array[j]:
        temp = array[i]
        array[i] = array[j]
        array[j] = temp

  return array

print(f'unsorted array : {numbers}')

bubbleSort(numbers)

print(f'sorted array : {numbers}')
