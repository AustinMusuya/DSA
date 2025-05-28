"""
# Merge Two Sorted Linked Lists

## Problem Statement

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a sorted manner and return the merged list.

---

## Example

**Input:**  
`list1 = [1, 2, 4]`  
`list2 = [1, 3, 4]`

**Output:**  
`[1, 1, 2, 3, 4, 4]`

---

## Constraints

- The number of nodes in both lists is in the range `[0, 50]`
- `-100 <= Node.val <= 100`

---

## Approach

- Use two pointers to iterate through both lists.
- Compare values and build a new list or modify one of the existing lists in-place.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n + m)
- **Space Complexity:** O(1) if done in-place, else O(n + m)

"""

# step1: create linked list


class Node():
    def __init__(self, value: int):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def add(self, value: int):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def first(self) -> int:
        if self.head:
            return self.head.value

    def remove_first(self):
        if self.head:
            # remove the first node
            temp = self.head.next
            self.head.next = None
            self.head = temp

        self.length -= 1

    def __str__(self) -> str:
        array = []

        if self.head is None:
            return "[]"

        if self.head.next is None:
            array.append(str(self.head.value))
            return "".join(array)

        current_node = self.head
        while current_node:
            array.append(str(current_node.value))
            current_node = current_node.next

        string_array = " --> ".join(array)
        return f"{string_array} | length : {self.length}"


new_list = LinkedList()
new_list.add(1)
new_list.add(2)
new_list.add(4)
new_list.add(5)
new_list.add(8)

new_list2 = LinkedList()
new_list2.add(1)
new_list2.add(4)
new_list2.add(5)
new_list2.add(6)
new_list2.add(7)
new_list2.add(10)


print(new_list)
print(new_list2)


# Merging the two lists in sorted format

# 1 --> 2 --> 4 --> 5 --> 8 | length : 5

# 4 --> 5 --> 6 --> 7 --> 10 | length : 5


def merge_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    # edge case: if either list is empty
    if list1.length == 0:
        return list2

    if list2.length == 0:
        return list1

    # step1: create a new empty linked list
    sorted_list = LinkedList()

    # Step2: iterate through both lists pushing the lesser value onto our new list
    while list1.length > 0 and list2.length > 0:

        if list1.first() <= list2.first():
            sorted_list.add(list1.first())
            list1.remove_first()
        else:
            sorted_list.add(list2.first())
            list2.remove_first()

    # add remaining elements
    while list1.length > 0:
        sorted_list.add(list1.first())
        list1.remove_first()

    while list2.length > 0:
        sorted_list.add(list2.first())
        list2.remove_first()

    return sorted_list


print(merge_lists(new_list2, new_list))

# Note: This approach has O(n) time and O(n) space complexity.
# We create a new list and new nodes instead of reusing existing ones.
# An in-place merge (relinking nodes) would reduce space to O(1).
