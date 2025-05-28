/*
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

*/

// Approach: Two pointer (slow, fast)
// Step1: Begin by creating the Node class for our linked list
// A node is characterized by having a value and a pointer to the next node
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}
// Step2: Create the linked list class with a head and tail as the initial nodes
// Our custom linked list will have a starting value when instatiated.
// A linked list is characterized to have a head and a tail node with other nodes in between.
class LinkedList {
  constructor(value) {
    this.head = new Node(value);
    this.tail = this.head;
    this.length = 1; //add length variable to update the size of the linked list
  }
  // Step 3: create method to add new nodes onto our custom linked list
  // We add a new node to the end of the linked list. The new node becomes our new tail.
  // we update the length variable +1
  add(value) {
    const newNode = new Node(value);
    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;
  }
  // Bonus step: represent our linked list data in the form of a string when printed to the console
  toString() {
    //method runs in O(n) space and time
    let currentNode = this.head;
    let array = [];
    while (currentNode) {
      array.push(currentNode.value);
      currentNode = currentNode.next;
    }
    return array.join(" --> ");
  }
  // Step 4: Apply our 2 pointer approach logic
  find_middle() {
    // two variables, fast and slow that traverse the nodes at different speeds.
    // Since fast traverses at twice as fast as slow, by the time it reaches the end, the slow one will
    // be at the middle node. we return the value of the slow node.
    let slow = this.head;
    let fast = this.head;
    while (fast && fast.next) {
      slow = slow.next;
      fast = fast.next.next;
    }
    return slow.value;
  }
}

const new_list = new LinkedList(42);

new_list.add(48);
new_list.add(82);
new_list.add(25);
new_list.add(37);

console.log(new_list.toString());
console.log(new_list.find_middle());

// Note : this is a much more reliable approach that will be consistent regardless of a wrong length
// variable data. complexities are O(n) for time and O(1) space
