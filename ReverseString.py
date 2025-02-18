# Try reverse a string of characters in python

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