# 创建一个generator，有很多方法。只要把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(10))

print(g)

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# generator也是可迭代对象
for n in g:
    print(n)


tu = (0, 1, 2, 3, 4)
print(tu[1])


a, b = 1, 2

print(a, b)


# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print('b is %d' % b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


for n in fib(6):
    print('数是%d' % n)


def san(max):
  n, p, no = 0, [1], [1]
  while n < max:
    print('now is %s' % no)
    print('jkj', n)
    yield no
    # if (n <= 2):
    #   p = no
    #   for x in range(n):
    #     no[x] = 1
    # else:
    #    pass
    #    no = [1]
    #    for x in p:
    #      if (x + 1 > p):
    #        no.append(1)
    #      else:
    #         pass
    #         no.append(p[x] + p[x + 1])
    n += 1
  return 'done'

for x in san(5):
  print(x)