#list comprehension

x = [1, 2, 3, 4, 5]
y = []

for i in x:
    y.append(i**2)

print(x)
print(y)

z = [i**2 for i in x]
print(z)

w = [i for i in x if i % 2 != 0]

print(w)