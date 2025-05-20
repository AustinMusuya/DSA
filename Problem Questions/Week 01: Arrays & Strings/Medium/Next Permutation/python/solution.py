"""
# Next Permutation

**Difficulty:** Medium  
**Topics:** Arrays, Two Pointers  
**Companies:** Multiple

---

## 📝 Problem Description

A **permutation** of an array of integers is an arrangement of its members 
into a sequence or linear order.

For example, for `arr = [1, 2, 3]`, the following are all the permutations of `arr`:

```text
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
```

The **next permutation** of an array of integers is the next lexicographically 
greater permutation of its integers.

More formally, if all the permutations of the array are sorted in a container 
according to their lexicographical order, 
then the next permutation is the one that follows it in the sorted order.

If such arrangement is **not possible**, the array must be rearranged as the 
**lowest possible order** (i.e., sorted in ascending order).

You must do this **in-place** and use **only constant extra memory**.

---

## 🔁 Examples

### Example 1

**Input:**

```text
nums = [1, 2, 3]
```

**Output:**

```text
nums = [1, 3, 2]
```

### Example 2

**Input:**

```text
nums = [3, 2, 1]
```

**Output:**

```text
nums = [1, 2, 3]
```

### Example 3

**Input:**

```text
nums = [1, 1, 5]
```

**Output:**

```text
[1, 5, 1]
```

"""

"""
Approach: 
 Step 1: Find the "break point"
 
    Find the first number from the right that is smaller than its next number.

    Start from the right side and move left.

    You're looking for the first pair where nums[i] < nums[i+1].

    This is the point where the ascending trend from the right breaks.

Step 2: Find the "next greater number" to swap with

    From the right again, find the smallest number greater than the number at the break point.

    This ensures you make the smallest possible increase.

 From [1, 3, 5, 4, 2], since 3 is the break point,

    Look to the right: [5, 4, 2]

    The next greater number than 3 is 4

Swap 3 and 4 → [1, 4, 5, 3, 2]

Step 3: Reverse the suffix

    Reverse everything to the right of the break point (i.e., after where the swap happened).

    Why? Because you want the next smallest order, and everything after the break point was in descending order (largest possible).

 After swap: [1, 4, 5, 3, 2]
Reverse [5, 3, 2] → becomes [2, 3, 5]

Final result: [1, 4, 2, 3, 5]
"""

from typing import List
nums = [1, 2, 3]


def next_permutation(array: List[int]) -> List[int]:
    size = len(array)
    break_point = -1

    # Step 1: Find the "break point" (rightmost index where array[i] < array[i + 1])
    for i in range(size - 2, -1, -1):
        if array[i] < array[i + 1]:
            break_point = i
            break

    # If no break point, it's the last permutation. Return first (sorted) permutation.
    if break_point == -1:
        array.reverse()
        return array

    # Step 2: Find the next greater element to the right of break point
    for i in range(size - 1, break_point, -1):
        if array[i] > array[break_point]:
            # Step 3: Swap
            array[i], array[break_point] = array[break_point], array[i]
            break

    # Step 4: Reverse the suffix
    array[break_point + 1:] = reversed(array[break_point + 1:])
    return array


print(next_permutation([1, 3, 5, 4, 2]))
print(next_permutation([1, 4, 2, 3, 5]))
print(next_permutation([1, 4, 2, 5, 3]))

# Note: This code can be made cleaner
