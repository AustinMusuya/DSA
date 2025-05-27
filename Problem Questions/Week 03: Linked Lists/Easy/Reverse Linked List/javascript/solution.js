/*
# Reverse a Linked List

## Problem Statement

Given the `head` of a singly linked list, 
reverse the list and return the new head.

---

## Example

**Input:**  
`head = [1, 2, 3, 4, 5]`

**Output:**  
`[5, 4, 3, 2, 1]`

*/

// step1: Create nodes

/*
Represent our nodes as a class with a value 
and pointer (next), that points to the next node.
*/

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

// step2: create custom linked list
/*
Represent our linked list as a class, with field variables head, tail and length. 
The list will have a beginning value once instatiated.
*/

class LinkedList {
  constructor(value) {
    this.head = new Node(value);
    this.tail = this.head;
    this.length = 1;
  }
  // step3: create function to append nodes to our linked list.
  append(value) {
    const newNode = new Node(value);
    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;
    return this;
  }
  // bonus step: create function to print linked list representation.
  toString() {
    let array = [];
    let currentNode = this.head;
    while (currentNode) {
      array.push(currentNode.value);
      currentNode = currentNode.next;
    }
    return array.join(" -> ");
  }
  // step4: create function to reverse linked list
  /*
  initialize two key variables. prevNode & nextNode
  while the nextNode is not null, we change the pointer direction to the previous node,
  shift our prevNode into our nextNodes position, shift our nextNode to our next, nextNode.
  finally we update our head and tail nodes.
  */
  reverse() {
    // edge case: single value in linked list
    if (this.length == 1) {
      return this.head;
    }

    let prevNode = this.head;
    let nextNode = prevNode.next;
    while (nextNode) {
      let temp = nextNode.next;
      nextNode.next = prevNode;
      prevNode = nextNode;
      nextNode = temp;
    }
    //update our head and tail nodes
    this.tail = this.head;
    this.head.next = null;
    this.head = prevNode;
  }
}

my_list = new LinkedList(12);
my_list.append(53);
my_list.append(3);
my_list.append(43);
console.log(my_list.toString());
my_list.reverse();
console.log(my_list.toString());
