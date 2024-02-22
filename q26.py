# Python program to count positive and negative numbers in a list


a = int(input())
b = int(input())

p = []
n = []

for i in range(a, b + 1):
    if i > 0:
        p.append(i)
    else:
        n.append(i)

print(len(p))
print(len(n))
