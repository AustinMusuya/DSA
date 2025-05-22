"""
# Merge Sort

## Problem Statement

Implement the **Merge Sort** algorithm to sort an array `nums` in ascending order.

Return the sorted array.

---

## Example

**Input:**  
`nums = [38, 27, 43, 3, 9, 82, 10]`

**Output:**  
`[3, 9, 10, 27, 38, 43, 82]`

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach

- Divide the array into halves recursively.
- Merge sorted halves using a two-pointer technique.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)

"""

# This is a recursive function tha uses the divide and conquer techninque
# Very effective and has Time & Space of O(nlogn), O(n)
# Space is linear becuase we return a newly sorted and merged array
from typing import List


def merge_sort(array: List[int]) -> List[int]:
    # Step 1: Create a base case for if sub array has a single value
    if len(array) <= 1:
        return array

    # Step 2: Recursive steps
    # We divide the array into two parts, left and right and keep on doing so,
    # until we hit our base case.
    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])

    # Step 3: we return the merged & sorted array
    return merge(left, right)

# Create logic for merging sub-arrays


def merge(left: List[int], right: List[int]) -> List[int]:
    # Step1: we need a an array to store the final result of the merged & sorted sub-arrays.
    sorted_array = []

    # Step 2: we compare the values of elements in the two arrays, and push the lesser one first
    # into our new array. We keep on doing this till there are no more values left to push.
    leftIndex, rightIndex = 0, 0

    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            sorted_array.append(left[leftIndex])
            leftIndex += 1
        else:
            sorted_array.append(right[rightIndex])
            rightIndex += 1

    # Looking for any left over values in our left sub-array and pushing them to our new array.
    while leftIndex < len(left):
        sorted_array.append(left[leftIndex])
        leftIndex += 1

    # Doing the same for the remainder values in the right sub-array. (if any)
    while rightIndex < len(right):
        sorted_array.append(right[rightIndex])
        rightIndex += 1

    return sorted_array


print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
print(merge_sort([]))
print(merge_sort([38]))
print(merge_sort([64, 87, 9, 7, 8, 2, 1, 6, 4, 3, 0, 10, 21]))
