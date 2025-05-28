"""
# Remove Duplicates from a Sorted Linked List

## Problem Statement

Given the `head` of a **sorted** linked list, delete all duplicates 
such that each element appears only once.

Return the linked list **without duplicates**.

---

## Example

**Input:**  
`head = [1, 1, 2, 3, 3]`

**Output:**  
`[1, 2, 3]`

---

## Constraints

- The number of nodes in the list is in the range `[0, 300]`
- `-100 <= Node.val <= 100`

---

## Approach

- Traverse the list with one pointer.
- If the current node’s value equals the next node’s value, skip the next node.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

"""

# step 1 : create a linked list

class Node():
    def __init__(self,value: int):
        self.value = value 
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def add(self, value: int):
       
        # empty linked list
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1

    def __str__(self):
        array = []
        if self.head is None:
            return "[]"
        
        current_node = self.head
        while current_node:
            array.append(str(current_node.value))
            current_node = current_node.next

        return " --> ".join(array)
    
    # Approach: shift the pointer to skip the next node 
    # when currentnode value is equal to the next node value

    def remove_duplicates(self):
        current_node = self.head

        while current_node and current_node.next:
            if current_node.value == current_node.next.value:
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                current_node = current_node.next
    
my_list = LinkedList()
print(my_list)
my_list.add(1)
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(3)



print(my_list)

my_list.remove_duplicates()
print(my_list)

my_list2 = LinkedList()
my_list2.add(1)
my_list2.add(1)
my_list2.add(2)
my_list2.add(3)
my_list2.add(3)
my_list2.add(3)

print(my_list2)

my_list2.remove_duplicates()
print(my_list2)