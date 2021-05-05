def utopianTree(n):
    h = 1
    for i in range(n):
        if i % 1:
            h += 1
        else:
            h += 2
    return h

print(utopianTree(10))
