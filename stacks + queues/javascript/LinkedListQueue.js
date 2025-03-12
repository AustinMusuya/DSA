class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.first = null;
    this.last = null;
    this.length = 0;
  }

  peek() {
    return this.first;
  }

  enqueue(value) {
    const newNode = new Node(value);

    if (this.length === 0) {
      this.first = newNode;
      this.last = newNode;
      this.first.next = this.last;
    } else {
      this.last.next = newNode;
      this.last = newNode;
    }

    this.length++;

    return this;
  }

  dequeue() {
    if (!this.first) return null;
    if (this.last === this.first) {
      this.last = null;
    }
    this.first = this.first.next;
    this.length--;
    return this;
  }

  //isEmpty
}

const myStack = new Queue();

myStack.enqueue(20);
myStack.enqueue(80);
myStack.enqueue(16);
myStack.enqueue(50);
myStack.enqueue(40);

myStack.enqueue(90);

myStack.dequeue();
myStack.dequeue();
myStack.dequeue();
myStack.dequeue();
// myStack.dequeue();
// myStack.dequeue();
// myStack.dequeue();

console.log(myStack);
