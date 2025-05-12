# Two Sum

## Problem Statement

Given an array of integers `nums` and an integer `target`, return **indices** of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and **you may not use the same element twice**.

You can return the answer in **any order**.

---

## Example

**Input:**  
`nums = [2, 7, 11, 15]`, `target = 9`

**Output:**  
`[0, 1]`  
**Explanation:** `nums[0] + nums[1] == 2 + 7 == 9`

---

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- Exactly one solution exists.

---

## Follow-up

Can you come up with an algorithm that runs in `O(n)` time?

---

## Approach

### Optimized (Hash Map):

- Initialize an empty hash map to store seen numbers and their indices.
- Iterate through `nums`:
  - For each element `nums[i]`, calculate its complement as `target - nums[i]`.
  - If the complement exists in the map, return `[map[complement], i]`.
  - Otherwise, store `nums[i]` in the map with its index.

This approach works in a single pass and is efficient for large inputs.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)  
  One pass through the array with constant-time hash map lookups.

- **Space Complexity:** O(n)  
  In the worst case, we store all elements in the hash map.

---

## Alternate Approach (Brute Force)

- Use two nested loops to check all pairs `(i, j)` such that `nums[i] + nums[j] == target`.
- Return `[i, j]` when a valid pair is found.

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)
