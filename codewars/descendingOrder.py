'''
Input a number and return the highest possible values for that set of numbers
'''

def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))

print(descending_order(0))
print(descending_order(15))
print(descending_order(123456789))
