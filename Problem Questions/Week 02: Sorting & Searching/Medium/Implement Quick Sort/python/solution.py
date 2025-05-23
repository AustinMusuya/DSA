"""
# Quick Sort

## Problem Statement

Implement the **Quick Sort** algorithm to sort an array `nums` in ascending order.

Return the sorted array.

---

## Example

**Input:**  
`nums = [10, 7, 8, 9, 1, 5]`

**Output:**  
`[1, 5, 7, 8, 9, 10]`

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach

- Choose a pivot.
- Partition the array such that elements less than pivot go left, greater go right.
- Recursively sort left and right halves.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n log n) average, O(n²) worst-case
- **Space Complexity:** O(log n) due to recursion stack

"""

# This is an unstable recursive algorithm that uses a pivoting technique to sort elements
# in the required non-decreasing order. The pivot is picked as the last element in the sequence
# (according to my technique). Elements larger than the pivot are placed into the right subarray,
# while elements smaller than the pivot are placed into the left subarray.
# Once we get to the smallest subarray, we merge them back up into our final array
# observing our pivot positions.

# Note: This approach will only be Time: O(nlogn) if our recursive calls keep picking good pivots.
# i.e (elements that are not the largest or the smallest).

from typing import List


def quick_sort(array: List[int]) -> List[int]:
    # Step1: create our base case.
    if len(array) <= 1:
        return array

    # Step 2: order our recursive steps
    pivot = array[-1]  # last element will be our pivot
    left = []
    right = []
    # loop through array up until the second-to-last element,
    # pushing values onto the left and right subarrays.
    for i in array[:-1]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort([5, 7, 9, 2, 1, 3, 645, 89, 65, 31]))
print(quick_sort([5]))
print(quick_sort([]))
