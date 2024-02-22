# Python program to print even numbers in a list

n = eval(input())

l = []
for i in range(n):
    if i % 2 == 0:
        l.append(i)

print(l)
