b = ['cat', 'dog']
c = [1, 4, 2, 8, 3]
a = b+c
a.append('cow')
print(a)
print(a[1])
print(a[1:])
a[1] = 'hen'
print(a)
print(len(a))
print(max(c))
print(sum(c))
print(min(c))
print(sorted(c))
"""" average of a number"""
avg = sum(c)/len(c)
print(avg)