# Python program to count Even and Odd numbers in a List

n = eval(input())
e = []
o = []

for i in n:
    if i % 2 == 0:
        e.append(i)
    else:
        o.append(i)

print(len(e))
print(len(o))
