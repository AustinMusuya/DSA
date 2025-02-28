class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.top = null;
    this.bottom = null;
    this.length = 0;
  }

  peek() {
    return this.top;
  }

  push(value) {
    const newNode = new Node(value);

    if (this.length === 0) {
      this.bottom = newNode;
      this.top = newNode;
    } else {
      const holdingPoint = this.top;
      this.top = newNode;
      this.top.next = holdingPoint;
    }

    this.length++;

    return this;
  }

  pop() {
    if (!this.top) return null;
    if (this.top === this.bottom) {
      this.bottom = null;
    }
    // const holdingpoint = this.top;
    this.top = this.top.next;
    this.length--;
    return this;
  }

  //isEmpty
}

const myStack = new Stack();

myStack.push("Discord");
myStack.push("Netflix");
myStack.push("Google");
myStack.push("Facebook");
myStack.push("Twitter");
myStack.push("Udemy");

myStack.pop();
myStack.pop();
myStack.pop();
myStack.pop();
myStack.pop();
myStack.pop();
myStack.pop();

console.log(myStack);
