# Try reverse a string of characters in python

# Approach: we try add the string values in reverse order by looping through them
#  and storing in an array. Then we convert the array back to string and return that value.

# 1.Iterate over the values or individual values from the last to the first
# and add to an empty array.

introduction = "Hi I am Austin and I rule baby!"

def reverseString(string):
    emptyList = []
    lastValue = len(string) - 1
    firstValue = 0

    while lastValue >= firstValue:
        emptyList.append(string[lastValue])
        lastValue -= 1
    reverse = ''.join(emptyList)

    return reverse

print(reverseString(introduction))