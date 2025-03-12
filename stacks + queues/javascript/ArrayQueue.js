// Try to implement a queue using 2 arrays

/*
Approach: So what we know about queues is they follow the FIFO principle.
we will try to use one array labeled as first, and so here is where we will push our values.
The second array we will name last, and we will also push our values here as well.
At any given moment either array will be empty and the other full of values.
Depending on the method called, (enqueue: add a value to the end of the array),
(dequeue: remove the first element of the array)
we will try to achieve O(n) time complexity.
*/

class ArrayQueue {
  constructor() {
    this.first = [];
    this.last = [];
  }

  enqueue(value) {
    // this should add an element to the end of the array
    this.first.push(value);
    return this;
  }

  dequeue() {
    //this should remove the first element
    for (let i = this.first.length - 1; i >= 0; i--) {
      this.last.push(this.first.pop());
    }
    this.last.pop();
    return this;
  }

  peek() {
    if (this.last.length > 0) {
      return this.last[this.last.length - 1];
    }
    return this.first[0];
  }

  isEmpty() {
    return this.first.length === 0 && this.last.length === 0;
  }
}

myArrayQueue = new ArrayQueue();

myArrayQueue.enqueue(54);
myArrayQueue.enqueue(80);
myArrayQueue.enqueue(16);
myArrayQueue.enqueue(12);

myArrayQueue.dequeue();
myArrayQueue.enqueue(54);
myArrayQueue.enqueue(80);
myArrayQueue.enqueue(16);
myArrayQueue.enqueue(12);

myArrayQueue.dequeue();
console.log(myArrayQueue);
