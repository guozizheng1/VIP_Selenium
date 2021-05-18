array = [98, 100, -100, -32, 39, 0, 85]

lst = []

for x in array:
    if x < 0:
        lst.append(x)

print(lst)
a = sum(lst[:])
print(a)
