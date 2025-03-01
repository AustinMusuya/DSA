class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
            self.bottom = newNode
        else:
            holdingPoint = self.top
            self.top = newNode
            self.top.next = holdingPoint

        self.length += 1
        return self

    def pop(self):
       if self.top is None:
           return None
       if self.top == self.bottom:
           self.bottom = None

       popped_value = self.top.value
       self.top = self.top.next
       self.length -= 1
       return popped_value
    
    def __str__(self):
        array = []
        currentNode = self.top
        while currentNode is not None:
            array.append(currentNode.value)
            currentNode = currentNode.next

        return f"Stack {array} | Top: {self.top.value} | Bottom: {self.bottom.value}"


myStack = Stack()

myStack.push(50)
myStack.push(40)
myStack.push(80)
myStack.push(16)
# myStack.pop()


print(myStack)