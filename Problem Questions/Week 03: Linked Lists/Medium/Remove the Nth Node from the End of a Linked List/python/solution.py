"""
# Remove Nth Node From End of List

## Problem Statement

Given the head of a linked list, 
remove the nth node from the end of the list and return its head.

---

## Example

**Input:**  
`head = [1,2,3,4,5], n = 2`  
**Output:**  
`[1,2,3,5]`

---

## Constraints

- The number of nodes in the list is `sz`
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

---

## Approach

- Use a two-pointer technique: advance one pointer `n` steps ahead.
- Move both pointers until the first one hits the end.
- The second pointer will be right before the node to remove.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

"""

# create a linked list


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def add(self, value: int):
        new_node = Node(value)

        # empty list
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def __str__(self):
        array = []

        # empty list
        if not self.head:
            return "[]"

        current_node = self.head
        while current_node:
            array.append(str(current_node.value))
            current_node = current_node.next

        return " --> ".join(array)

    def remove_from_end(self, position: int):
        # Approach: Use the two pointer technique

        # edge case 1 : out of bounds position
        if position <= 0 or position > self.length:
            raise ValueError(
                f"Invalid position {position}. Must be between 1 and {self.length}.")

        # Step1 : we need a dummy node so we don't ovewrite our head
        dummy = Node(0)
        dummy.next = self.head

        first = dummy
        second = dummy
        # step 2: loop through the range of the position and move first by the same number of steps

        for _ in range(position):
            first = first.next  # first moves n times ahead

        # step 3: move first and second nodes while first.next node is not none
        while first.next:
            first = first.next
            second = second.next

        # step 4: now that we have the value to remove we shift the pointers
        unwanted_node = second.next
        second.next = second.next.next

        # edge case 1: if our value to remove was the tail
        if unwanted_node == self.tail:
            self.tail = second

        # edge case 2: if our value to remove was the head
        self.head = dummy.next

        # update the length
        self.length -= 1


new_list = LinkedList()

for val in [50, 42, 37, 46, 13, 12, 130]:
    new_list.add(val)


print(new_list)
new_list.remove_from_end(6)

print(new_list)
