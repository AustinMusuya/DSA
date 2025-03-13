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

  traverseToIndex(index) {
    let counter = 0;
    let currentNode = this.head;
    while (counter != index) {
      currentNode = currentNode.next;
      counter++;
    }
    return currentNode;
  }

  bubbleSort() {
    if (!this.head || !this.head.next) {
      return this;
    }

    let swapped = true; // Ensure the loop runs at least once
    while (swapped) {
      swapped = false; // Reset swap flag at the start of each pass
      let currentNode = this.head;

      while (currentNode.next) {
        if (currentNode.value > currentNode.next.value) {
          // Swap values
          let temp = currentNode.value;
          currentNode.value = currentNode.next.value;
          currentNode.next.value = temp;

          swapped = true; // If swap happens, continue looping
        }
        currentNode = currentNode.next;
      }
    }

    return this;
  }
}

const myLinkedList = new LinkedList();

myLinkedList.append(115);
myLinkedList.append(120);
myLinkedList.append(40);
myLinkedList.append(20);
myLinkedList.append(60);
myLinkedList.prepend(40);
myLinkedList.bubbleSort();

console.log(myLinkedList.printList());
