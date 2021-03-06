'''
#Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

(Use the English alphabet with 26 letters!)
'''

def find_missing_letter(chars):
    if chars[0].isupper():
        s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    else:
        s = 'abcdefghijklmnopqrstuvwxyz'
    s = s[s.index(chars[0]):s.index(chars[0])+len(chars)+1]
    return [e for e in s + ''.join(chars) if e not in s or e not in ''.join(chars)][0]

#print(find_missing_letter(['a','b','c','d','f']))
print(find_missing_letter(['L','N','O','P','Q']))

'''
def find_missing_letter(chars):
    return [chr(n) for n in range(ord(chars[0]),ord(chars[-1])+1) if n not in [ord(c) for c in chars]][0]

def find_missing_letter(c):
    return next(chr(ord(c[i])+1) for i in range(len(c)-1) if ord(c[i])+1 != ord(c[i+1]))
'''
