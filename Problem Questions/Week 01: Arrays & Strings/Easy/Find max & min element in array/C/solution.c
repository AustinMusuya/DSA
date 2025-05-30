/*
# Find Maximum and Minimum in Array

## Problem Statement

Given an array of integers,
return the **maximum** and **minimum**
elements in the array.

---

## Example

**Input:**
`nums = [3, 1, 5, 9, 0, -3]`

**Output:**
`max = 9, min = -3`

---
*/

#include <stdio.h>

// function prototype:
void findMaxMin(int *array, int length, int *min, int *max);

int main()
{
    // usage
    int nums[] = {21, 78, 32, 4, 6, 23, 3, 12, 1, 2};
    int min, max;
    int length = sizeof(nums) / sizeof(nums[0]);

    findMaxMin(nums, length, &min, &max);

    printf("Min: %d, Max: %d\n", min, max);

    return 0;
}

// Approach: Grab a page off selection sort logic
void findMaxMin(int *array, int length, int *min, int *max)
{
    // Step 1: Initialize a max and min variable at index 0
    *min = array[0];
    *max = array[0];

    // Step 2: Loop through array updating the values,
    // when a new max or min is found.
    for (int i = 0; i < length; i++)
    {
        if (array[i] < *min)
        {
            *min = array[i];
        }
        if (array[i] > *max)
        {
            *max = array[i];
        }
    }
}
