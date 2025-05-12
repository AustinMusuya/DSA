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
