"""
# Majority Element

## Problem Statement

Given an array `nums` of size `n`, return the **majority element**. The majority element is the element that appears **more than ⌊n / 2⌋ times**.

You may assume that the majority element **always exists** in the array.

---

## Example

**Input:**  
`nums = [3, 2, 3]`

**Output:**  
`3`

---

**Input:**  
`nums = [2, 2, 1, 1, 1, 2, 2]`

**Output:**  
`2`

---

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`
- The majority element always exists.

---

## Approach

- Use the **Boyer-Moore Voting Algorithm**:
  - Initialize `count = 0` and a candidate.
  - If count drops to 0, select the current element as candidate.
  - Increment or decrement count based on match with candidate.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

"""
from typing import List

nums = [2, 2, 1, 1, 1, 2, 2]

# Boyer-Moore Voting Algorithm:
"""
This algorithm finds a potential majority element in linear time and constant space.
Core idea:
- Maintain a candidate and a counter.
- If the counter is 0, select the current element as the new candidate.
- If the current element equals the candidate, increment the counter.
- Otherwise, decrement the counter.
After one pass, the candidate is only a *potential* majority.
A second pass is required to confirm it appears more than n // 2 times.
"""


def majority_element(array: List[int]) -> int:
    # edge cases:Empty
    if not array:
        return -1

    # Using a for loop
    candidate = -1  # initialize our first element as the candidate

    count = 0  # votes start at zero for any given candidate

    for i in array:
        if count == 0:
            candidate = i
            count = 1
        elif i == candidate:
            count += 1
        else:
            count -= 1

    count = 0

    for i in array:
        if i == candidate:
            count += 1

    if count > len(array) // 2:
        return candidate
    return -1


print(majority_element([2, 2, 1, 1, 1, 2, 2]))

print(majority_element([2, 2, 1, 1, 1, 1, 1, 2, 2]))
print(majority_element([2, 2, 3, 3]))
print(majority_element([2]))
print(majority_element([]))
print(majority_element([4, 4, 4, 4, 4, 4]))
