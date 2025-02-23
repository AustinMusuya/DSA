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
}

let myLinkedList = new LinkedList(50);

myLinkedList.append(10);
myLinkedList.append(40);
myLinkedList.append(30);

myLinkedList.prepend(70);

console.log(myLinkedList.prinList());
