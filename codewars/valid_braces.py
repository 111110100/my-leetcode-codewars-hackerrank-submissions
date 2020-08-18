'''
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
'''

def valid_brace(s):
    r, opened = '', 0
    for c in s:
        if c in '({[' and opened > 0:
            r += c
        if c in ')}]' and opened > 1:
            r += c
        opened +=1 if c in '({[' else -1
    #return not bool(opened)
    return [opened, r]

print(valid_brace('(){}[]'))
print(valid_brace('[(])'))
print(valid_brace('([{}])'))
