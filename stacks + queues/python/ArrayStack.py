class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.stack = []

    def peek(self):
        return self.stack[len(self.stack) - 1]
    
    def push(self, value):
        if len(self.stack) == 0:
            self.stack.append(value)
            self.bottom = value
        else:
            self.stack.append(value)
            self.top = self.stack[len(self.stack) - 1]

    def pop(self):
        self.stack.pop()
        self.top = self.stack[len(self.stack) - 1]

    def __str__(self):
        return f"Stack {self.stack} | Top: {self.top} | Bottom: {self.bottom}"


myStack = Stack()
myStack.push("Austin")
myStack.push("James")
myStack.push("Brian")
myStack.push("Mark")
myStack.push("Nick")

myStack.pop()

print(myStack)