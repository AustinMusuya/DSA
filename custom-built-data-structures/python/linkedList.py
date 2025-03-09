# 10 ---> 50 ---> 40 ---> null

# Creating a simple structure of how we want our linkedlist to be
# head being the start then value and pointer to the next node

linkedList = {
    'head': {
        'value': 50,
        'next': {  # this is a node to the next value
            'value': 10,
            'next': {
                'value': 20,
                'next': None
            }
        }
    }
}

# Approach: Create a class that takes the value as the constructor parameter.
# Next create a class variable (head) of an object that takes the value and has a pointer to the next node.
# create a tail that points to the memory address of the head variable
# create a class variable length that starts at value 1

# method: Append
# create a method, append(value), takes value as parameter. This should atleast try to add a new node to the linked list
# point the tail.next value to the newNode memory address, and change the value to the newNode thereafter
# increament the length class variable by one then return the object


# method: Prepend
# create a method, prepend(value), takes value as parameter. This should atleast try to add a new node to the head of the linked list
# point the newNode.next value to the head memory address, and change the value of the head to the newNode thereafter
# increament the length class variable by one then return the object


# method: printList
# 1.create a method, printList(). This should atleast try to represent the value of linked list
# in an array.

# 2. Create an empty array.

# 3. Create a variable to show the currentNode and set it equal to the head of the linked list.

# 4. Create a while loop for whenever the currentNode isn't null/none,
# you add the currentNode.value to the array

# 5. Set the currentNode equal to the currentNode.next

# 6. Return the array after exiting the loop


class LinkedList():
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newNode = {
            'value': value,
            'next': None
        }
        self.tail['next'] = newNode
        self.tail = newNode
        self.length += 1

        return self

    def prepend(self, value):
        newNode = {
            'value': value,
            'next': None
        }
        newNode['next'] = self.head
        self.head = newNode
        self.length += 1

        return self

    # def printList(self):
    #     array = []
    #     currentNode = self.head
    #     while currentNode is not None:
    #         array.append(currentNode['value'])
    #         currentNode = currentNode['next']

    #     return array
    
    def __str__(self):
        array = []
        currentNode = self.head
        while currentNode is not None:
            array.append(currentNode['value'])
            currentNode = currentNode['next']

        return f"LinkedList | length: {self.length} | {array} | Head: {self.head['value']} | Tail : {self.tail['value']}"
    
    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)  # Ensures the instance is returned

        newNode = {'value': value, 'next': None}
        leader = self.traverseToIndex(index - 1)
        newNode['next'] = leader['next']
        leader['next'] = newNode
        self.length += 1
        return self

    def traverseToIndex(self, index):
        counter = 0
        currentNode = self.head

        while counter != index:
            currentNode = currentNode['next']
            counter += 1

        return currentNode

    def remove(self, index):
        if index == 0:
            self.head = self.head['next']  # Properly update head
            self.length -= 1
            return self

        previousNode = self.traverseToIndex(index - 1)
        unwantedNode = previousNode['next']
        previousNode['next'] = unwantedNode['next']
        if previousNode['next'] is None:  # Update tail if last node is removed
            self.tail = previousNode
        self.length -= 1
        return self
    
    def reverse(self):
        if self.length == 1:
            return self.head
        
        self.tail = self.head
        first = self.head
        second = first['next']

        while second:
            temp = second['next']
            second['next'] = first
            first = second
            second =  temp

        self.head['next'] = None
        self.head = first
        return self


mylinkedList = LinkedList(50)

mylinkedList.append(10)
mylinkedList.append(40)
mylinkedList.append(30)
mylinkedList.append(20)

print(mylinkedList)

mylinkedList.insert(2, 80)

print(mylinkedList)

mylinkedList.remove(0)

print(mylinkedList)

mylinkedList.reverse()

print(mylinkedList)
