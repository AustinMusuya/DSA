
# ARRAYS

# Try to recreate an array using python classes with a few functions.

'''
 Expected output

 {
     length: 4,
     data: {
         0: value1,
         1: value2,
         2: value3,
     },
 }
'''

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

# LINKED-LISTS

# Try to recreate a linked list using python classes with a few functions.


# Approach:
'''
 1. Create a class that takes the value as the constructor parameter.

 2. Next create a class variable (head) of an object that takes the value 
    and has a pointer to the next node.
 
 3. Create a tail that points to the memory address of the head variable
 
 4. Create a class variable length that starts at value 1
'''

# method: Append
'''
 1. Create a method, append(value), takes value as parameter.
 (This should atleast try to add a new node to the linked list)

 2. Point the tail.next value to the newNode memory address, and change the value of the tail to the newNode thereafter
 
 3. Increament the length class variable by one then return the object
'''

# method: Prepend
'''
 1. Create a method, prepend(value), takes value as parameter. 
 (This should atleast try to add a new node to the head of the linked list)
 
 2. Point the newNode.next value to the head memory address, and change the value of the head to the newNode thereafter.
 
 3. Increament the length class variable by one then return the object.
'''

# method: insert
'''
 1. Create a method, insert(index, value), takes index & value as parameters. 
 (This should atleast try to add a new node to a specific index of the linked list)
 
 2. Point the newNode.next value to the head memory address, and change the value of the head to the newNode thereafter.
 
 3. Increament the length class variable by one then return the object.
'''

# method: remove
'''
 1. Create a method, remove(index), takes value as parameter. 
 (This should atleast try to remove an existing node at a specific index of the linked list)
 
 2. Point the newNode.next value to the head memory address, and change the value of the head to the newNode thereafter.
 
 3. Increament the length class variable by one then return the object.
'''


# method: printList
'''
 1. Create a method, printList().
 This should atleast try to represent the value of linked list in an array.

 2. Create an empty array.

 3. Create a variable to show the currentNode and set it equal to the head of the linked list.

 4. Create a while loop for whenever the currentNode isn't null/none,
 you add the currentNode.value to the array

 5. Set the currentNode equal to the currentNode.next

 6. Return the array after exiting the loop
 
'''
