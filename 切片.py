l = ['a', 'b', 'c', 'd']

a = list(range(100))
# print(type(a))
print(a[1:3])
print(a)

# from collections import Iterable

# print(isinstance('adc', Iterable))

for i, val in enumerate(l):
    print(i)

c = [1, 2, 3, 4, 5, 6]

print('min is %d' % min(c))


ll = [(1, 2), (4, 5), (7, 8)]

for x, y in ll:
  print(x, y)