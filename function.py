def a():
    print('123')
a()

b = [0,1,2,3,4,5][0:3]

print(isinstance(21, (int)))

print(b)



def testManyReturns():
  return 1,2,3,4


print(testManyReturns())
test1, test2, test3, test4 = testManyReturns()

print('test1 is %s' % (test1))

def ab(a = []):
  a.append('END')
  return a

print(ab())
print(ab())


def abc(name, **kw):
  print('other:', kw)
abc('123', **{'a': 'dsd', 'b': 'cs'})