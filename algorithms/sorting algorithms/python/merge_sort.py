

# Merge sort
'''
The approach here is divide and conquer. We first split the array into two halves recursively
until we are left with individual elements in single arrays. We then compare values on which is less
and which is more, where the former is pushed to a new array first and the latter is pushed thereafter.
The array is then merged or unwound iteratively with such comparisons till
we get the full array as sorted


Visualized breakdown and merge for mergesort algorithm

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

# left              #right
[99, 44, 6, 2, 1,],  [5, 63, 87, 283, 4, 0]

# Left side

# splitting
[99, 44, 6, 2, 1]

[99, 44], [6, 2, 1 ],

[99], [44], [6], [2, 1 ]

[99], [44], [6], [2], [1],

# merging

[44, 99] , [6], [2], [1],

[44, 99] , [6], [1, 2]

[44, 99] , [1,2,6]

[1, 2, 6, 44, 99]

# Right side

# splitting
[5, 63, 87, 283, 4, 0]

[5, 63, 87] [283, 4, 0]

[5] [63, 87] [283], [4, 0]

[5], [63], [87] [283], [4], [0]

# merging
[5], [63,87], [283] [0, 4]

[5, 63, 87], [0, 4, 283]

[0, 4, 5, 63, 87, 283]

# Left                           #Right
[1, 2, 6, 44, 99]               [0, 4, 5, 63, 87, 283]

[0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]

'''


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def merge_sort(array):
    #   base case
    if len(array) <= 1:
        return array

    # divide and conquer
    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    return merge(merge_sort(left), merge_sort(right))  # recursive case


def merge(left, right):
    leftIndex = 0
    rightIndex = 0
    result = []

    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1

    # adding the remaining elements

    while leftIndex < len(left):
        result.append(left[leftIndex])
        leftIndex += 1

    while rightIndex < len(right):
        result.append(right[rightIndex])
        rightIndex += 1

    # result.extend(left[leftIndex:]) #cleaner
    # result.extend(right[rightIndex:])

    return result


print(merge_sort(numbers))

# print(numbers[0: len(numbers)//2])

# print(numbers[len(numbers)//2: len(numbers)])
