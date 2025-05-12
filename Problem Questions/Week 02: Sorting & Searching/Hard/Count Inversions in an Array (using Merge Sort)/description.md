# Count Inversions in an Array

## Problem Statement

Given an array `nums`, count the number of **inversions** in the array.

An inversion is a pair `(i, j)` such that `i < j` and `nums[i] > nums[j]`.

---

## Example

**Input:**  
`nums = [2, 4, 1, 3, 5]`

**Output:**  
`3`  
**Explanation:** The inversions are (2,1), (4,1), and (4,3)

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach

- Use a modified **Merge Sort** algorithm to count the number of inversions during the merge step.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)
