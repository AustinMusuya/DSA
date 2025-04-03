"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9

"""
nums = [2, 7, 11, 15]

# Optimized Approach (hashmap) Time Complexity O(1): Space Complexity O(n)
"""
We will loop through the array and store each value to a hashmap/dictionary 
in the (key:value) pair of (number:index) in the array. (i.e, 2 : 0, 7 : 1 )

A variable "complement" that is the target sum minus the array[i] i.e (9 - 2 = 7) 
will be compared to see if it is existent in the hashmap/dicitionary.

If it is then we will return an array of the two indices [0, 1] 

If not we will keep on adding values till the end of the array 
and return an empty array if we cannot find the sum pair indices

"""


def two_sum(array, target):
    map = {}
    for i in range(len(array)):
        complement = target - array[i]
        if complement in map:
            return [map[complement], i]
        map[array[i]] = i

    return []


print(two_sum(nums, 9))


# Brute Force Approach nested loop Time Complexity O(n^2): Space Complexity O(1)
"""
We will have two loops (outer and inner) where we will check to see if array[i] is equal to 
array[j]

if so then we will return the two indices of the elements in the array

Input: nums = [2,7,11,15], target = 9

"""


def two_sum2(array, target):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                return [i, j]

    return []


print(two_sum2(nums, 9))
