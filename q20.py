# Python program to print all even numbers in a range

n = eval(input())

l = []

for i in range(1, n + 1):
    if i % 2 == 0:
        l.append(i)

print(l)
