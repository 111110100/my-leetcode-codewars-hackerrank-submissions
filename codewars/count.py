'''
Write a function that takes an array and counts the number of each unique element present.

count(['james', 'james', 'john']) 
#=> { 'james' => 2, 'john' => 1}
'''

def count(array):
    d = {}
    for v in set(array):
        d[v] = array.count(v)
    return d

print(count(['james', 'james', 'john']))

'''
def count(array):
    return {x: array.count(x) for x in array}

def count(array):
    return {x:array.count(x) for x in set(array)}
'''