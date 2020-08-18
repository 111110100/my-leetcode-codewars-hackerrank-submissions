'''
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes:

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
'''

def high_and_low(numbers):
    n = [int(l) for l in numbers.split(" ")]
    return f'{max(n)} {min(n)}'

print(high_and_low("1 2 -3 4 5"))

'''
def high_and_low(numbers):
    n = numbers.split(' ')
    n = [int(l) for l in n]
    n.sort()
    return f'{n[len(n)-1]} {n[0]}'

def high_and_low(numbers):
    n = [int(l) for l in numbers.split(" ")]
    return f'{max(n)} {min(n)}'

def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

def high_and_low(numbers):
  n = map(int, numbers.split(' '))
  return str(max(n)) + ' ' + str(min(n))
'''