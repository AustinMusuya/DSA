numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


"""
Approach: Counting sort
Time Complexity: O(k + n)
Space complexity: O(k)

"""


def counting_sort(array):
    size = len(array)

    max_number = max(array)

    counts = [0] * (max_number + 1)

    for i in array:
        counts[i] += 1

    i = 0

    for x in range(max_number + 1):
        while counts[x] > 0:
            array[i] = x
            i += 1
            counts[x] -= 1

    return array


print(counting_sort(numbers))
