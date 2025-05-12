# Merge two sorted arrays into one sorted array.

array1 = [0, 3, 4, 31]
array2 = [3, 4, 6, 30]
array3 = []


def mergeSortedArrays(arr1, arr2):
    # check input and edge cases
    # if either of the arrays is empty

    if not arr1:
        return arr2
    if not arr2:
        return arr1

    # Approach: check and compare the first elements in each array,
    # then put the least value of the two into a new array

    i, j = 0, 0  # Pointers for both arrays
    mergedArray = []

    # Merge elements in sorted order
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            mergedArray.append(arr1[i])
            i += 1
        else:
            mergedArray.append(arr2[j])
            j += 1

    # Append remaining elements from arr1 (if any)
    while i < len(arr1):
        mergedArray.append(arr1[i])
        i += 1

    # Append remaining elements from arr2 (if any)
    while j < len(arr2):
        mergedArray.append(arr2[j])
        j += 1

    return mergedArray


print(array1)
print(array2)
print(mergeSortedArrays(array1, array2))
