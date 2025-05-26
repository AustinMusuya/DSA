"""
# Reverse a Linked List

## Problem Statement

Given the `head` of a singly linked list, reverse the list and return the new head.

---

## Example

**Input:**  
`head = [1, 2, 3, 4, 5]`

**Output:**  
`[5, 4, 3, 2, 1]`

---

## Constraints

- The number of nodes in the list is in the range `[0, 5000]`
- `-5000 <= Node.val <= 5000`

---

## Approach

- Use an iterative approach with three pointers: `prev`, `current`, and `next`.
- Rewire the `next` pointers as you traverse the list.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

"""

# Approach: First let us create our custom linked list
# Reversing the list:
# we simply change the pointers direction from head to tail, then update our new head and tail


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Linkedlist():
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

        return self

    def __str__(self):
        array = []
        currentNode = self.head
        while currentNode is not None:
            array.append(currentNode.value)
            currentNode = currentNode.next

        return f"LinkedList | {array} | Head: {self.head.value} | Tail : {self.tail.value}"

    # Lets add function to reverse our current arrangement
    def reverse(self):
        # edge case: single node in list
        if self.length == 1:
            return self.head
        # step 1; Change the pointers direction
        self.tail = self.head
        first = self.head
        second = first.next

        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp

        self.head.next = None
        self.head = first
        return self


new_list = Linkedlist(15)

new_list.append(45)
new_list.append(54)
new_list.append(65)
new_list.append(25)

new_list.reverse()

print(new_list)
