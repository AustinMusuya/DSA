// 10 ---> 50 ---> 40 ---> null

// Creating a simple structure of how we want our linkedlist to be
// head being the start then value and pointer to the next node

let sampleLinkedlist = {
  head: {
    value: 10,
    next: {
      value: 50,
      next: {
        value: 40,
        next: null,
      },
    },
  },
};

// Approach: Create a class that takes the value as the constructor parameter.
// Next create a class variable (head) of an object that takes the value and has a pointer to the next node.
// create a tail that points to the memory address of the head variable
// create a class variable length that starts at value 1

// method: Append
// create a method, append(value), takes value as parameter. This should atleast try to add a new node to the tail of the linked list
// point the tail.next value to the newNode memory address, and change the value to the newNode thereafter
// increament the length calss variable by one then return the object

// method: Prepend
// create a method, prepend(value), takes value as parameter. This should atleast try to add a new node to the head of the linked list
// point the newNode.next value to the head memory address, and change the value of the head to the newNode thereafter
// increament the length class variable by one then return the object

// method: printList
// create a method, printList(). This should atleast try to represent the value of linked list in an array.
// create an empty array. Create a variable to show the currentNode and set it equal to the head of the linked list.
// create a while loop  for whenever the currentNode isn't null/none, you add the currentNode.value to the array
// set the currentNode equal to the currentNode.next
// return the array after exiting the loop

class LinkedList {
  constructor(value) {
    this.head = {
      value: value,
      next: null,
    };
    this.tail = this.head;
    this.length = 1;
  }

  append(value) {
    const newNode = {
      value: value,
      next: null,
    };
    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;
    return this;
  }

  prepend(value) {
    const newNode = {
      value: value,
      next: null,
    };
    newNode.next = this.head;
    this.head = newNode;
    this.length++;
    return this;
  }

  prinList() {
    const array = [];
    let currentNode = this.head;
    while (currentNode != null) {
      array.push(currentNode.value);
      currentNode = currentNode.next;
    }
    return array;
  }

  reverse() {
    if (this.length === 1) {
      return this.head;
    }
    this.tail = this.head;
    let first = this.head;
    let second = first.next;

    while (second) {
      const temp = second.next;
      second.next = first;
      first = second;
      second = temp;
    }
    this.head.next = null;
    this.head = first;

    return this;
  }

  insert(index, value) {
    if (index >= this.length) {
      return this.append(value);
    }
    const newNode = {
      value: value,
      next: null,
    };
    const leader = this.traverseToIndex(index - 1);
    const holdingPointer = leader.next;
    leader.next = newNode;
    newNode.next = holdingPointer;
    this.length++;

    return this.prinList();
  }

  traverseToIndex(index) {
    let counter = 0;
    let currentNode = this.head;
    while (counter != index) {
      currentNode = currentNode.next;
      counter++;
    }
    return currentNode;
  }

  remove(index) {
    if (index >= this.length) {
      return undefined;
    }
    const previousNode = this.traverseToIndex(index - 1);
    const unwantedNode = previousNode.next;
    previousNode.next = unwantedNode.next;
    this.length--;

    return this.prinList();
  }
}

let myLinkedList = new LinkedList(50);

myLinkedList.append(10);
myLinkedList.append(40);
myLinkedList.append(30);
myLinkedList.prepend(70);

console.log(myLinkedList.prinList());

myLinkedList.insert(2, 80);

console.log(myLinkedList.prinList());

myLinkedList.remove(2);

console.log(myLinkedList.prinList());
myLinkedList.reverse();

console.log(myLinkedList.prinList());
