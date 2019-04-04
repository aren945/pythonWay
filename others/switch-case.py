switcher = {
	0: 'this is 0',
	1: 'this is 1',
	2: 'this is 2'
}

num = switcher[2]  # 如果访问没有的属性会报错

# 使用get方法

num2 = switcher.get(4, 'Unkown')

print(num)
print('num2 is %s' % num2)
