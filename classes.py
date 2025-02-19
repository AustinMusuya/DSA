# Try to recreate an array using javascript classes with a few functions.

class MyArray():
    def __init__(self, length=0, data={}):
        self.length = length
        self.data = data

    def append(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self, index):
        del self.data[index]
        self.length -= 1

    def __str__(self):
        return f"{self.length} , {self.data}"


newArray = MyArray()

print(newArray)

newArray.append('Hi')
newArray.append('I')
newArray.append('am')
newArray.append('Austin')
newArray.append('Musuya')
newArray.pop(4)


print(newArray)
