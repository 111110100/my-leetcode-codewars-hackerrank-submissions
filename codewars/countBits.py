'''
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''

def countBits(n):
    return bin(n).count('1')

print(countBits(12345))

'''
def countBits(n):
    total = 0
    while n > 0:
        total += n % 2
        n >>= 1
    return total

def countBits(n):
    total = 0
    while n > 0:
        total += n & 2
        n >>= 1
    return total
'''