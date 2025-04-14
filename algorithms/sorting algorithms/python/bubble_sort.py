numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

"""
Bubble Sort

Bubble Sort is a simple comparison-based sorting algorithm that repeatedly steps through the array, 
compares adjacent elements, and **swaps them if they are in the wrong order**.

The largest value "bubbles up" to its correct position at the end of the array in each outer loop iteration.
This process is repeated until the array is sorted.

---

🧠 Logic Approach:
- Use two nested loops:
  - Outer loop keeps track of passes (we need n-1 passes for n elements).
  - Inner loop compares each pair of adjacent items and swaps them if needed.
- After every complete pass, the largest unsorted element is at the end.
- To optimize: If in any pass, no elements are swapped → the array is already sorted, and we can **break early**.

💡 Optimization: A `swapped` flag is used to check whether any swaps occurred in the current pass.
If not, we stop the algorithm early since the array is sorted.

---

🔍 Visualized step-by-step breakdown:

Initial array:
[5, 3, 8, 4, 2]

Pass 1:
→ Compare 5 & 3 → swap → [3, 5, 8, 4, 2]  
→ Compare 5 & 8 → no swap  
→ Compare 8 & 4 → swap → [3, 5, 4, 8, 2]  
→ Compare 8 & 2 → swap → [3, 5, 4, 2, 8]  
End of Pass 1: largest number 8 is now at the end.

Pass 2:
→ Compare 3 & 5 → no swap  
→ Compare 5 & 4 → swap → [3, 4, 5, 2, 8]  
→ Compare 5 & 2 → swap → [3, 4, 2, 5, 8]  
End of Pass 2: second-largest 5 is in place

Pass 3:
→ Compare 3 & 4 → no swap  
→ Compare 4 & 2 → swap → [3, 2, 4, 5, 8]  
→ Compare 4 & 5 → no swap  
End of Pass 3

Pass 4:
→ Compare 3 & 2 → swap → [2, 3, 4, 5, 8]  
→ No swaps in next comparisons

Pass 5:
→ No swaps at all → array is sorted, exit early

Final sorted array:
[2, 3, 4, 5, 8]

---

📉 Time Complexity:
- Worst & Average: O(n²)
- Best Case (already sorted): O(n) with early exit optimization

📦 Space Complexity: O(1) — sorts in-place  
🔁 Stable: ✅ (relative order of equal elements is preserved)

"""


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    return array


def the_real_bubble_sort(array):
    size = len(array)
    for i in range(size - 1):
        swapped = False  # Set a boolean flag to track swaps
        for j in range((size - 1) - i):  # Reduce the range after every outer loop iteration
            if array[j] > array[j+1]:
                # Swap adjacent Elements
                [array[j], array[j+1]] = [array[j+1], array[j]]
                swapped = True
        if not swapped:  # Exit if no swaps (already sorted)
            break

    return array


print(f'unsorted array : {numbers}')

the_real_bubble_sort(numbers)

print(f'sorted array : {numbers}')
