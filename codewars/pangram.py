'''
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation
'''

def is_pangram(s):
    m = {}
    n = list(map(chr, range(97, 123)))
    for c in s.lower():
        if c not in m and c in n:
            m[c] = 1
    return len(m) == 26

'''
import string

def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())


import string

def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True


def is_pangram(s):
    return True if set('abcdefghijklmnopqrstuvwxyz').issubset(set(s.lower())) else False

'''
