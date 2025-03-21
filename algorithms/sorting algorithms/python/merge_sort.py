numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def merge_sort(array):
    if len(array) <= 1:  # base case
        return array

    # get the middle of the array
    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]
    return merge(merge_sort(left), merge_sort(right))  # recursive case


def merge(left, right):
    left_index = 0
    right_index = 0
    result = []

    while left_index < len(left) and right_index < len(right):

        if (left[left_index] < right[right_index]):
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


print(merge_sort(numbers))
