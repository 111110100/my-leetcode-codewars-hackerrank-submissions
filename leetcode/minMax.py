a = [1, 2, 3, 4, 5]

aa = [sum(a) - a[i] for i in range(len(a))]
print(sum(a))
print(aa)
print(min(aa), max(aa))
