# Try to recreate an array using javascript classes with a few functions.


#  Approach:

# 1. Setup
'''  
Create a class with constructor with field variables of length and data.
Set the variables to 0 and an empty object/map respectively
'''

# 2. Push Method. (adds item to the end of the list/array)
''' 
Create a push method to add value to the data object.[length] key and increment the length variable by 1
'''

# 3. Pop Method.(removes the last item)
''' 
 Create a pop method to delete the last added value at the data.length key (data[this.length - 1]),
and decrement the length variable by 1
'''

# 4. Shift Method. (Removes the first item)
''' 
   If the length is 0 then return undefined as the output
   Set a variable index to the value of 0.
   Loop through the elements while the last item is greater than the index, 
   storing the data at index + 1 (data[index + 1]), in data at the current index (data[index])
   then increment index by 1
   Delete the last item and decrement the length by 1
   Return the first item
'''

# 5. Unshift method (adds an item to the begin of array/list)
'''
    Set variable index and set it to the length of the array.
    Loop through the array while the length of the array/list is more than 0.
    Store the value of data[index -1] to data[index] and decrement the value of index
    set data[0] to the value passed as the parameter.
    Increment the length by 1
'''


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

    def unshift(self, value):
        index = self.length

        while index > 0:
            # shifts value to the right
            self.data[index] = self.data[index - 1]
            index -= 1

        self.data[0] = value

        self.length += 1

        return self

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
newArray.unshift(500)


print(newArray)
