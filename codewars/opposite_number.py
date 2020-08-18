'''
Very simple, given a number, find its opposite.

Examples:

1: -1
14: -14
-34: 34
'''

def opposite(number):
    return abs(number) if number < 0 else number - (number * 2)

print(opposite(1))

'''
def opposite(number):
    return -number

def opposite(number):
  return number * -1
'''