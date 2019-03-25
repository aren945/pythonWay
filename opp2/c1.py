class Student():
	# 类属性
	name = 'static name'
	age = 0

	def __init__(self, name, age):
		'''构造函数'''
		# 实例化的时候会自动调用构造方法

		# 实例变量
		self.name = 'zheng' + name
		self.age = age
		self.__gender = 'man'  # 私有的

	def print_file(self):
		print('name: %s' % self.name)
		print('age: %s' % self.age)


	def say_fn(self):
		print(self.__gender)

	# 类方法
	@classmethod
	def plus_sum(cls):
		print(cls)
		pass

	# 静态方法
	@staticmethod
	def add():
		print('this is static method')


st1 = Student(age='10', name="xinglun")
st2 = Student(age='123', name="xinglun123")

st1.print_file()

print(st1.name)
print(Student.name)
print(st2.name)
print(Student.name)

st1.plus_sum()
Student.plus_sum()

st1.add()

st1.__gender = 'woman'
st1.say_fn()
print(st1.__dict__)

