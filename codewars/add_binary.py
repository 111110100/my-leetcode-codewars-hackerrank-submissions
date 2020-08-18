def add_binary(a, b):
    return bin(a + b).split('b')[1]


print(add_binary(64, 128))

'''
def add_binary(a,b):
    return '{:b}'.format(a+b)

def add_binary(a,b):
    return f'{a+b:b}'
'''