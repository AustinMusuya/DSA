# Try to recreate an array using javascript classes with a few functions.


#  Approach:
#  Create a class with constructor with field variables of length and data.
#  Set the variables to 0 and an empty object/map respectively

#  Push Method.
#  Create a push method to add value to the data object.[length] key and increment the length variable by 1

#  Pop Method.
#  Create a pop method to delete the last added value at the  data.length key and decrement the length variabel by 1

#  Shift Method.

#  If the length is 0 then return undefined as the output
#  Set a variable index to the value of 0.
#  Loop through the elements while the last item is greater than the index, storing the data at index + 1 in data at the index then increment index by 1
#  Delete the last item and decrement the length by 1
#  Return the first item

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

    def shift(self):
        if self.length == 0:
            return None

        lastItem = self.length - 1
        firstItem = self.data[0]
        index = 0

        while index < lastItem:
            self.data[index] = self.data[index + 1]
            index += 1

        del self.data[self.length - 1]
        self.length -= 1

        return firstItem

    def __str__(self):
        return f"{self.length} , {self.data}"


newArray = MyArray()

print(newArray)

newArray.append('Hi')
newArray.append('I')
newArray.append('am')
newArray.append('Austin')
newArray.append('Musuya')
print(newArray)
newArray.pop(4)
print(newArray)
newArray.shift()


print(newArray)
