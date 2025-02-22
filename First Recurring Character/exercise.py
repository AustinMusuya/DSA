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



print(firstRecurring([2,5,1,2,3,5,1,2,4]))
print(firstRecurring([2,1,1,2,3,5,1,2,4]))
print(firstRecurring([2,3,4,5]))