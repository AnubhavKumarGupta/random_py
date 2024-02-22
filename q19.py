# Python program to print odd numbers in a List

n = eval(input())

l = []
for i in range(n):
    if i % 2 != 0:
        l.append(i)

print(l)
