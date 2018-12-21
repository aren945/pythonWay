try:
  f = open('logger.log', 'r')
  print(f.read())
finally:
  if f:
    f.close()

# 会自动调用f.close(),跟try...finally一样
with open('logger.log', 'r') as f1:
  print(f1.read())


with open('logger.log', 'r') as f1:
  for index, line in enumerate(f1.readlines()):
    print('%s行：%s' % (index, line), end='')