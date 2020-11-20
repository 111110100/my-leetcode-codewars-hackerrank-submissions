l1 = [1, 2, 4, 5]
l2 = [4, 5, 6, 7]

l1_diff, l2_diff = [], []

for x, y in zip(l1, l2):
    if x not in l2:
        l1_diff.append(x)
    if y not in l1:
        l2_diff.append(y)

print(l1_diff, l2_diff)