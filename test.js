class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = this.head;
    this.length = 0;
  }

  append(value) {
    const newNode = new Node(value);
    if (this.length == 0) {
      this.head = newNode;
      this.tail = this.head;
    }

    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;

    return this;
  }

  printList() {
    const array = [];
    let currentNode = this.head;

    while (currentNode != null) {
      array.push(currentNode.value);
      currentNode = currentNode.next;
    }
    return array;
  }

  prepend(value) {
    const newNode = new Node(value);

    if (this.length == 0) {
      this.head = newNode;
      this.tail = this.head;
    }

    const holdingPoint = this.head;
    this.head = newNode;
    this.head.next = holdingPoint;
    this.length++;
    return this;
  }
  /*
  remove(value) {
    let currentNode = this.head;
    let index = 0;
    while (currentNode != null) {
      if (currentNode.value === value) {
        let previousNode = this.traverse(index - 1);
        let nextNode = this.traverse(index + 1);
        previousNode.next = nextNode;
      }
      currentNode = currentNode.next;
      index++;
    }
    this.length--;
    return this;
  }
*/
  remove(value) {
    if (!this.head) return this; // If list is empty, return

    // Handle removal of the head node
    if (this.head.value === value) {
      this.head = this.head.next;
      this.length--;
      return this;
    }

    let currentNode = this.head;
    let previousNode = null;

    while (currentNode) {
      if (currentNode.value === value) {
        previousNode.next = currentNode.next; // Bypass the node
        this.length--;
        return this; // Exit after first removal
      }
      previousNode = currentNode;
      currentNode = currentNode.next;
    }

    return this; // Return list if value is not found
  }

  traverse(index) {
    let counter = 0;
    let currentNode = this.head;
    while (counter != index) {
      currentNode = currentNode.next;
      counter++;
    }
    return currentNode;
  }
}

const myLinkedList = new LinkedList();

myLinkedList.append(115);
myLinkedList.append(120);
myLinkedList.append(40);
myLinkedList.append(20);
myLinkedList.append(60);
myLinkedList.prepend(40);

console.log(myLinkedList);
console.log(myLinkedList.printList());
myLinkedList.remove(20);
// myLinkedList.remove(60);
// myLinkedList.remove(20);
console.log(myLinkedList.printList());
myLinkedList.remove(60);
console.log(myLinkedList.printList());
// console.log(myLinkedList.traverse(4));
