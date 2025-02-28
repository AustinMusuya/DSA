class Stack {
  constructor() {
    this.items = [];
  }

  peek() {
    return this.items[this.items.length - 1];
  }

  push(value) {
    this.items.push(value);
    return this;
  }

  pop() {
    this.items.pop();
    return this;
  }
}

const myStack = new Stack();

myStack.push(20);
myStack.push(80);
myStack.push(16);
myStack.push(50);
myStack.push(40);

console.log(myStack.push(90));

console.log(myStack.peek());
console.log(myStack.pop());
