numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


# Insertion Sort

'''
The approach here is similar to how you sort cards in your hand: you pick the next card (element),
compare it with the ones already sorted (to its left), and insert it in the correct position by shifting
larger elements to the right.

We move through the array from left to right, assuming that the portion on the left is already sorted.
At each step, we take the "key" (the current value), and compare it with elements to its left.
As long as those elements are larger than the key, we shift them one position to the right.
Once we find the correct spot, we insert the key.

This method avoids repeated swapping and is more efficient than a purely swap-based version.

---

Visualized step-by-step process for insertion sort:

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

Initial:
[99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

Step 1: Compare 44 with 99 → Insert 44 before 99
[44, 99, 6, 2, 1, 5, 63, 87, 283, 4, 0]

Step 2: Compare 6 with 99, 44 → Insert before both
[6, 44, 99, 2, 1, 5, 63, 87, 283, 4, 0]

Step 3: Compare 2 with 99, 44, 6 → Insert at start
[2, 6, 44, 99, 1, 5, 63, 87, 283, 4, 0]

Step 4: Compare 1 with all → Insert at start
[1, 2, 6, 44, 99, 5, 63, 87, 283, 4, 0]

Step 5: Compare 5 with 99, 44, 6 → Insert between 2 and 6
[1, 2, 5, 6, 44, 99, 63, 87, 283, 4, 0]

Step 6: Compare 63 → Insert between 44 and 99
[1, 2, 5, 6, 44, 63, 99, 87, 283, 4, 0]

Step 7: Insert 87 between 63 and 99
[1, 2, 5, 6, 44, 63, 87, 99, 283, 4, 0]

Step 8: 283 is already in place
[1, 2, 5, 6, 44, 63, 87, 99, 283, 4, 0]

Step 9: Insert 4 between 2 and 5
[1, 2, 4, 5, 6, 44, 63, 87, 99, 283, 0]

Step 10: Insert 0 at the very start
[0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]

Final Sorted Array:
[0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]
'''

def insertion_sort(array):
    size = len(numbers)
    for i in range(1,size):
        key = array[i]
        j = i - 1

        while j>=0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        
        array[j+1] = key
    
    return array

print(insertion_sort(numbers))