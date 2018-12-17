import random

count = 0
randNum = random.randint(0,9)

while count < 3:
  num = int(input('输入数字>>>:'))
  if (num == randNum):
    print('随机数是%d' % randNum)
    break
  else:
    if (count == 2):
      choose = input('是否继续玩Y/N:')
      if (choose == 'Y'):
        count = 0
      else:
        break
    else:
      count += 1