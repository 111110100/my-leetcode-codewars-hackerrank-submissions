'''
Given a list of numbers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching "odd" or "even".

If the input array is empty consider it as: [0] (array with a zero).

Example:
odd_or_even([0])          ==  "even"
odd_or_even([0, 1, 4])    ==  "odd"
odd_or_even([0, -1, -5])  ==  "even"
'''

def odd_or_even(arr):
    return ['odd', 'eveb'][sum(arr) % 2 == 0]

'''
def oddOrEven(arr):
    return ('even', 'odd')[sum(arr) % 2]

oddOrEven = lambda l: "odd" if sum(l) % 2 else "even"
'''