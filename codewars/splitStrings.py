'''
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
'''
def split_strings(s):
    if len(s) % 2 != 0:
        s += '_'
    r = []
    for x in range(0, len(s), 2):
        r.append(s[x]+s[x+1])
    return r

print(split_strings('abcdefg'))

'''
def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result

def solution(s):
    return [s[x:x+2] if x < len(s) - 1 else s[-1] + "_" for x in range(0, len(s), 2)]

def solution(s):
    return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]

def solution(s):
    return list(map(''.join, zip(*[iter(s + '_')] * 2)))

solution = lambda s: list(map(''.join, __import__('itertools').zip_longest(* [iter(s)] * 2, fillvalue='_')))
'''
