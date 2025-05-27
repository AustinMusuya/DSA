"""
# Find the Middle of the Linked List

## Problem Statement

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the **second** middle node.

---

## Example

**Input:**  
`head = [1, 2, 3, 4, 5]`

**Output:**  
`3`

**Input:**  
`head = [1, 2, 3, 4, 5, 6]`

**Output:**  
`4`

---

## Constraints

- The number of nodes in the list is in the range `[1, 100]`
- `1 <= Node.val <= 100`

---

## Approach

- Use two pointers: slow and fast.
- Move fast by two steps and slow by one. When fast reaches the end, slow is at the middle.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

"""


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self, value: int):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def __str__(self) -> str:
        array = []
        current_node = self.head
        while current_node:
            array.append(str(current_node.value))
            current_node = current_node.next

        return " -> ".join(array)

# Finding the middle element
    def middle(self) -> int:
        mid = self.length // 2
        midValue = self.traverse_to_index(mid)

        return midValue

    def traverse_to_index(self, index: int) -> int:
        # traverse to the node index
        # edge case: out of bounds
        if index < 0 or index > self.length - 1:
            return -1

        # start point
        count, current_node = 0, self.head

        while current_node and count < index:
            current_node = current_node.next
            count += 1

        return current_node.value

# Note: This approach doesn't use two pointer approach.
# It returns the middle value of the linked list using stored length and index traversal.
# Time: O(n), Space: O(1)
# Relies on accurate maintenance of self.length.
# Less robust than the slow/fast pointer method but works well in controlled scenarios.


new_list = LinkedList(40)
new_list.append(80)
new_list.append(40)
new_list.append(48)
new_list.append(1020)

print(new_list)

# list =  40 -> 80 -> 40 -> 48 -> 1020


new_list2 = LinkedList(410)
new_list2.append(820)
new_list2.append(406)
new_list2.append(478)
new_list2.append(120)
new_list2.append(121)

print(new_list2)

# list2 =  410 -> 820 -> 406 -> 478 -> 120 -> 121

print(new_list2.middle())
