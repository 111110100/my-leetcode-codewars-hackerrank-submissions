'''
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
'''

def accum(s):
    n = list(s)
    m = []
    for i in range(len(n)):
        m.append(s[i].upper() + s[i].lower() * i)
    return '-'.join(m)

print(accum('abcd'))
print(accum('ZpglnRxqenU'))

'''
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
'''