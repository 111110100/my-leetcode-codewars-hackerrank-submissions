'''
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
'''

def get_count(input_str):
    num_vowels = 0
    vowels = 'aeiou' 
    for v in vowels:
        num_vowels += input_str.count(v)
    return num_vowels

print(get_count('abracadabra'))
print(get_count('pear tree'))

'''
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

def getCount(s):
    return sum(c in 'aeiou' for c in s)

'''