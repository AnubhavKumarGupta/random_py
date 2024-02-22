nums = [1, 15, 6, 3]
l= []
for i in nums:
    l.extend([int(digit) for digit in str(i)])
print(s-l)