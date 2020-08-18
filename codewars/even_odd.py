'''
Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
'''

def even_or_odd(number):
    return ['Odd', 'Even'][number % 2 == 0]

'''
def even_or_odd(number):
    return ['Odd', 'Even'][number % 2]

'''