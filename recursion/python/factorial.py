# Steps to achieve recursion

# 1. Identify the base case of the function
# so we can opt out when the condition is met and avoid filling up the callstack
# 2. Identify the recursive case (where we call the function within our function)
# 3. Get closer and closer and return when needed (so this means we'll have 2 return statements):
#      each for the base case and recursive case

'''
 
Example of Recursion use case


def inception():
    counter = 0
    if counter > 3:  # The if statement is the base case and returns done when the condition is met
        return "Done!"

    return inception() #This is the recursive case (function called within the function)


'''

# Exercise:
# Use recursion to get factorial of a number passed as the argument on your function call
# Have two approaches the recursive approach & iterative approach


# Recursive approach


# Iterative approach
