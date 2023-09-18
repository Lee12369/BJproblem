a = set()
a.add(1)
a.add(2)
b = set(a)
b -= {1}
print(a)
print(b)