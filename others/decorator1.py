import time
from functools import wraps

def decorator(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		print(time.time())
		return func(*args, **kwargs)
	return wrapper

@decorator
def f1():
	'''
	this is f1
	:return:
	'''
	print(f1.__name__)


print(help(f1))
# f1()