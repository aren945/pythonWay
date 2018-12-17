# while 被正常执行完，没有被break打断，会执行else语句
i = 0
while i < 3:
    print('%02d' % i)
    i += 1
else:
    print('else')
