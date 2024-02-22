# Python program to print all negative numbers in a range

a = int(input())
b = int(input())

l = []
for i in range(a, b + 1):
    if i < 0:
        l.append(i)

print(l)
