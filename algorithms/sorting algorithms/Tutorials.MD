# 🧠 Sorting Algorithms - Explanations & Logic

This document outlines the core concepts, logic, and characteristics of six common sorting algorithms:

- Bubble Sort
- Insertion Sort
- Selection Sort
- Merge Sort
- Quick Sort
- Counting Sort

---

## 🫧 Bubble Sort

<img align="center" width="1000" alt="Coding" src="https://www.lavivienpost.net/wp-content/uploads/2022/01/bubble-640.gif">

**Concept**: Repeatedly compares and swaps adjacent elements if they are in the wrong order. The largest value "bubbles up" to the end in each pass.

**Logic**:

- Loop through the array `n-1` times.
- On each pass, compare adjacent pairs and swap if needed.
- Use a `swapped` flag to break early if the array is already sorted.

**Best Case**: O(n)  
**Worst Case**: O(n²)  
**Space**: O(1)  
**Stable**: ✅

**Example**:

```
Initial: [5, 3, 8, 4, 2]
Pass 1 → [3, 5, 4, 2, 8]
Pass 2 → [3, 4, 2, 5, 8]
Pass 3 → [3, 2, 4, 5, 8]
Pass 4 → [2, 3, 4, 5, 8]
```

---

## 🪜 Insertion Sort

<img align="center" width="1000" alt="Coding" src="https://www.lavivienpost.net/wp-content/uploads/2022/01/insertion-600.gif">

**Concept**: Builds the sorted list one element at a time by comparing each new element with those already sorted and inserting it in the right spot.

**Logic**:

- Start at index 1.
- Use a `key` to hold the current value.
- Shift larger elements to the right to make space for `key`.

**Best Case**: O(n)  
**Worst Case**: O(n²)  
**Space**: O(1)  
**Stable**: ✅

**Example**:

```
Initial: [8, 5, 3, 1]
Pass 1 → [5, 8, 3, 1]
Pass 2 → [3, 5, 8, 1]
Pass 3 → [1, 3, 5, 8]
```

---

## 📌 Selection Sort

<img align="center" width="1000" alt="Coding" src="https://www.lavivienpost.net/wp-content/uploads/2022/01/selection-600.gif">

**Concept**: Selects the smallest (or largest) value from the unsorted part and swaps it into the correct position.

**Logic**:

- For each index `i`, assume it's the smallest.
- Traverse the rest of the array to find the real smallest.
- Swap it with `i`.

**Best/Worst Case**: O(n²)  
**Space**: O(1)  
**Stable**: ❌ (but can be modified to be stable)

**Example**:

```
Initial: [5, 3, 8, 2]
Pass 1 → [2, 3, 8, 5]
Pass 2 → [2, 3, 8, 5]
Pass 3 → [2, 3, 5, 8]
```

---

## 🔀 Merge Sort

<img align="center" width="1000" alt="Coding" src="https://www.lavivienpost.net/wp-content/uploads/2022/02/merge-sort-400.gif">

**Concept**: Divide-and-conquer. Recursively splits the array into halves, sorts each, and merges the results.

**Logic**:

- Recursively divide the array until each sub-array has one element.
- Merge sorted sub-arrays while comparing smallest elements.

**Best/Worst Case**: O(n log n)  
**Space**: O(n)  
**Stable**: ✅

**Example**:

```
Split: [4, 2, 1, 3] → [4,2] + [1,3] → [2,4] + [1,3]
Merge: [1,2,3,4]
```

---

## ⚡ Quick Sort

<img align="center" width="1000" alt="Coding" src="https://www.lavivienpost.net/wp-content/uploads/2022/02/quicksort-600-1.gif">

**Concept**: Divide-and-conquer. Picks a pivot and partitions elements into two groups — less than and greater than the pivot — then sorts those recursively.

**Logic**:

- Choose a pivot (e.g., last element).
- Rearrange elements so all values < pivot come before it.
- Recursively apply the above on sub-arrays.

**Best/Average Case**: O(n log n)  
**Worst Case**: O(n²) (when pivot is poorly chosen)  
**Space**: O(log n) average (due to recursion stack)  
**Stable**: ❌

**Example**:

```
Initial: [5, 3, 8, 2, 1]
Pivot = 1 → [ ] + [1] + [5, 3, 8, 2]
Pivot = 2 → [ ] + [2] + [5, 3, 8]
→ [1, 2, 3, 5, 8]
```

---

## 🧮 Counting Sort

<img align="center" width="1000" alt="Coding" src="https://miro.medium.com/v2/resize:fit:720/format:webp/0*B-CyBxmCVUolqSjj.gif">

**Concept**: Not based on comparisons. Counts occurrences of each unique element and uses this info to place elements in sorted order.

**Logic**:

- Find the max value in the array.
- Initialize a count array of size max+1.
- Count frequency of each value.
- Rebuild the sorted array using counts.

**Best/Worst Case**: O(n + k), where `k` = range of input  
**Space**: O(n + k)  
**Stable**: ✅  
**Limitation**: Only works for non-negative integers or when the range `k` is not excessively large.

**Example**:

```
Input: [4, 2, 2, 8, 3, 3, 1]
Counts: [0,1,2,2,1,0,0,0,1]
Result: [1,2,2,3,3,4,8]
```

---

## ✅ Summary Table

| Algorithm      | Best Case  | Average Case | Worst Case | Space    | Stable | Notes                                |
| -------------- | ---------- | ------------ | ---------- | -------- | ------ | ------------------------------------ |
| Bubble Sort    | O(n)       | O(n²)        | O(n²)      | O(1)     | ✅     | Easy to implement, inefficient       |
| Insertion Sort | O(n)       | O(n²)        | O(n²)      | O(1)     | ✅     | Good for small or mostly sorted data |
| Selection Sort | O(n²)      | O(n²)        | O(n²)      | O(1)     | ❌     | Fewest swaps, but always O(n²)       |
| Merge Sort     | O(n log n) | O(n log n)   | O(n log n) | O(n)     | ✅     | Consistent and reliable performance  |
| Quick Sort     | O(n log n) | O(n log n)   | O(n²)      | O(log n) | ❌     | Very fast with good pivots, unstable |
| Counting Sort  | O(n + k)   | O(n + k)     | O(n + k)   | O(n + k) | ✅     | Only for integers in small range     |

---
