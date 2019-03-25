if (0,):
  print(123123)


s = int(input(">>:"))

if s > 100:
  print('分数不对！')
elif s < 60: 
  print('分数%2d,不及格！' % s)
elif s < 80:
  print('分数%d,一般！' % s)
elif s <= 100:
  print('分数%d,优秀！' % s)

print("{0} {1} {0}".format('1', '2'))

i = 0
while i <=10:
  if i == 5:
    i+=1
    pass # 进行下一个循环
  print(i)
  i+=1 

print('''
dasd
dasd
dasds
''')


testNum = 3


def test_fn():
    print(testNum)


test_fn()
