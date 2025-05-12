# Allocate Minimum Pages

## Problem Statement

Given an array `pages[]` where `pages[i]` is the number of pages in the `i`th book, and `m` students, allocate books such that:

- Each student gets **at least one book**
- Books are allocated **contiguously**
- The **maximum number of pages assigned to a student is minimized**

Return this minimum value.

---

## Example

**Input:**  
`pages = [12, 34, 67, 90], m = 2`

**Output:**  
`113`  
**Explanation:** The books can be split as [12, 34, 67] and [90].

---

## Constraints

- `1 <= pages.length <= 10^5`
- `1 <= pages[i] <= 10^9`
- `1 <= m <= pages.length`

---

## Approach

- Use binary search on the answer space (from max(pages) to sum(pages)).
- Check feasibility of a mid value.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n log(sum))
- **Space Complexity:** O(1)
