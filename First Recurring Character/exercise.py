"""
Google Question
Given an array = [2,5,1,2,3,5,1,2,4]:
It should return 2

Given an array = [2,1,1,2,3,5,1,2,4]:
It should return 1

Given an array = [2,3,4,5]:
It should return undefined

"""

# Brute Force approach

def firstRecurring(input):
    size = len(input)
    for i in range(size):
        for j in range(i):
            if input[i]== input[j]:
                return input[i]
    return None



# print(firstRecurring([2,5,1,2,3,5,1,2,4]))
# print(firstRecurring([2,1,1,2,3,5,1,2,4]))
# print(firstRecurring([2,3,4,5]))

# Optimized approach (hashmap)

# Approach: 
# Loop through all the array elements and store in hashmap. 
# Upon looping ,Check if the key already exists in the map and return it. 
# Else add the element as the key, and its index as the value

def firstRecurring2(input):
    hashmap = {}
    for i in range(len(input)):
        if input[i] in hashmap:
            return input[i]
        else:
            hashmap[input[i]] = i
        
    return None

print(firstRecurring2([2,5,1,2,3,5,1,2,4]))
print(firstRecurring2([2,1,1,2,3,5,1,2,4]))
print(firstRecurring2([2,3,4,5]))
