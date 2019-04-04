'''
可迭代对象 迭代器
for in iterable

迭代器：
	可以被for in迭代
'''


# 将一个类转为可迭代对象

# 只要在class里面实现__iter__和__next__方法就可以

class IteratorBook(object):

	def __init__(self):
		self.data = ['book1', 'book2', 'book3']
		self.cur = 0

	def __iter__(self):
		return self

	def __next__(self):

		if self.cur >= len(self.data):
			raise StopIteration()

		r = self.data[self.cur]
		self.cur += 1
		return r


book = IteratorBook()

# for i in book:
# 	print(i)

print(next(book))

# 迭代器 重要特性 一次性！！！









# 生成器

def gen(max):
	n = 0
	while n <= max:
		# print(n)
		n += 1
		yield n


g = gen(10000)

# for i in g:
# 	print(i)

print(next(g))
