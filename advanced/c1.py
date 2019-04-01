# 函数式编程
# 闭包= 函数 + 环境变量

def cureve_pre():
	a = 10
	b = 30

	def curve(x):
		return a * x ** 2

	return curve


f = cureve_pre()
print(f(2))  # 40


class Pe():
	def test(self):
		pass


print(f.__closure__)
print(f.__closure__[0].cell_contents)

a = 0

def  fn2(x):
		global a
		b = a +x
		a = b
		return b


print(fn2(0))
print(fn2(1))
print(fn2(3))



def factory():
	aa = 0
	def add(x):
		# nonlocal 标记一个变量不是局部变量
		nonlocal aa
		aa += x
		return  aa
	return add

f11 = factory()
print('---------------------------------------')
print(f11(0))
print(f11(1))
print(f11(2))