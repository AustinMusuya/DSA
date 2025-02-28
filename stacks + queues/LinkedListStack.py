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
        newNode = {
            'value': value,
            'next': None
        }
        if self.length == 0:
            self.top = newNode
            self.bottom = newNode
        else:
            holdingPoint = self.top
            self.top = newNode
            self.top['next'] = holdingPoint

        self.length += 1
        return self

    def pop(self):
        pass


myStack = Stack()

myStack.push(50)
myStack.push(40)
myStack.push(80)
myStack.push(16)

print(myStack)