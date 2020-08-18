'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
'''

def find_short(s):
    return min(len(l) for l in s.split())

print(find_short("bitcoin take over the world maybe who knows perhaps"))

'''
def find_short(s):
    return len(min(s.split(' '), key=len))

def find_short(s):
    return min(map(len, s.split(' ')))
'''