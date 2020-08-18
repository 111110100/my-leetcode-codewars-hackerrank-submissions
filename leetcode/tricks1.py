cities = ['Manila', 'Singapore', 'Hing Kong']
for i, city in enumerate(cities):
    print(i, city)

l1 = [1, 4 ,5, 9, 0, 3, 4]
l2 = [5, 7 ,3, 8, 8, 2]
for a,b in zip(l1, l2):
    print(a, b)

v = [6, 9]
a, b = v 
print(a)
print(b)

print(l1[::-1])

l1, l2 = l2, l1
