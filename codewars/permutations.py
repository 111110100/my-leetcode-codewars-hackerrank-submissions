'''
In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
The order of the permutations doesn't matter.
'''

def permutations(s):
    m = []

    def heapsAlgo(a, l, r):
        if l == r:
            m.append(''.join(a))
        else:
            for i in range(l, r + 1):
                a[l], a[i] = a[i], a[l]
                heapsAlgo(a, l + 1, r)
                a[l], a[i] = a[i], a[l]
    
    heapsAlgo(list(s), 0, len(s) - 1)

    return sorted(list(set(m)))

def permutations2(s):
    if len(s) <= 1: return [s]
    else: return set(s[i]+p for i in range(len(s)) for p in permutations(s[:i] + s[i+1:]))

print(permutations('aabb'))


'''
def permutations(s):
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [s]
    else:
        return set(s[i]+p for i in range(len(s)) for p in permutations(s[:i] + s[i+1:]))

def permutations(s):
    if len(s) <= 1: return [s]
    else: return set(s[i]+p for i in range(len(s)) for p in permutations(s[:i] + s[i+1:]))

import itertools

def permutations(string):
    return map("".join(p) for p in set(itertools.permutations(string)))

from itertools import permutations as pm
permutations=lambda s: map(''.join, set(pm(s)))
'''