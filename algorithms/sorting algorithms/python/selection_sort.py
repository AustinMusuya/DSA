numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

"""
Selection Sort

The approach here is to iterate through the array and, at each step, **select the minimum element**
from the unsorted part of the array and swap it with the element at the current position.
This ensures that with every outer loop iteration, 
the smallest remaining element is moved to its correct position.

Unlike insertion sort which *shifts elements*, selection sort *selects* 
the minimum and swaps just once per pass.

This algorithm maintains two subarrays in the given array:
  1. The subarray which is already sorted.
  2. The remaining subarray which is unsorted.

---

🔍 Visualized step-by-step breakdown for Selection Sort:

Initial array:
[99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

Step 1:
Start at index 0 → current minimum = 99  
Find smaller values: 44 → 6 → 2 → 1 → 5 → ... → **0**  
Swap 0 with 99 → [0, 44, 6, 2, 1, 5, 63, 87, 283, 4, 99]

Step 2:
Start at index 1 → current minimum = 44  
Find smaller: 6 → 2 → **1**  
Swap 1 with 44 → [0, 1, 6, 2, 44, 5, 63, 87, 283, 4, 99]

Step 3:
Start at index 2 → current minimum = 6  
Find smaller: 2 → swap → [0, 1, 2, 6, 44, 5, 63, 87, 283, 4, 99]

Step 4:
Start at index 3 → current minimum = 6  
Find smaller: 5 → swap → [0, 1, 2, 5, 44, 6, 63, 87, 283, 4, 99]

Step 5:
Start at index 4 → current minimum = 44  
Find smaller: 6 → **4** → swap → [0, 1, 2, 5, 4, 6, 63, 87, 283, 44, 99]

Step 6:
Start at index 5 → already minimum → skip

Step 7:
index 6 → already minimum → skip

Step 8:
index 7 → already minimum → skip

Step 9:
index 8 → current minimum = 283  
Find smaller: **44** → swap → [0, 1, 2, 5, 4, 6, 63, 87, 44, 283, 99]

Step 10:
index 9 → current minimum = 283  
Find smaller: 99 → swap → [0, 1, 2, 5, 4, 6, 63, 87, 44, 99, 283]

Step 11:
Last index → sorted!

Sorted array:
[0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]

---

🧠 Logic summary:
- Outer loop selects position `i`
- Inner loop searches for the smallest element in the unsorted part
- Once found, swap it with the element at `i`
- Repeat until the entire array is sorted

📉 Time Complexity:  
Worst, Average, Best Case = O(n²)  
📦 Space Complexity: O(1) — in-place sort  
🔁 Stable: ❌ (can be made stable, but default implementation is not)
"""


def selectionSort(array):
    if len(array) == 0:
        return None
    size = len(array)
    for i in range(size):
        min = i
        for j in range(i+1, size):
            if array[j] < array[min]:
                min = j

        # swap the values min and first index
        (array[i], array[min]) = (array[min], array[i])

    return array


print(selectionSort(numbers))
