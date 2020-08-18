def duplicate_encode(word):
    s = ''
    word = word.lower()
    for c in word:
        if word.count(c) > 1:
            s += ')'
        else:
            s += '('
    return s

def duplicate_encode2(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

breakpoint()

print(duplicate_encode2('din'))
print(duplicate_encode2('recede'))
print(duplicate_encode2('Success'))
print(duplicate_encode2('(( @'))
