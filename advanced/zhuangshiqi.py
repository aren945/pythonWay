import time
import functools

def now(func):
	def wrapper(*args, **kw):
		print(time.time())
		return func(*args, **kw)

	return wrapper

@now
def f1():
	print('this is a function')

f1()


def d4(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('this is decorator4')
		return func(*args, **kw)

	return wrapper


def d5(text):
	def decorator(func):
		print('log is %s' % text)

		def wrapper(*args, **kw):
			print('asd')
			return func(*args, **kw)

		return wrapper

	return decorator


@d4
@d5('多个装饰器')
def foo4(a, b):
	print('a is %s, b is %s' % (a, b))


foo4(10, 20)

# 等效于 d5(d4(foo4(10, 20)))

def d1(text):
	def decorator(func):
		def wrapper(*args, **kwargs):
			print(text)
			return func(*args, **kwargs)
		return wrapper
	return decorator

@d1('hehe')
def f2():
	print("this is fn2")
	return  'this is return data'

res = f2()

print(res)