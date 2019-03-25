from opp2.People import People


class Student(People):

		# def __init__(self, score):
		# 	self.score = score

		# 方法一
		# def __init__(self, name, age, score):
		# 	self.score = score
		# 	People.__init__(self, name=name, age=age)

		# 方法二 子类调用父类的方法
		def __init__(self, name, age, score):
			self.score = score
			# ptyhon2
			# 第一个参数是当前的子类，第二个参数self
			# super(Student, self).__init__(name=name, age=age)
			super().__init__(name=name, age=age)

		def get_name(self):
			print(self.name)


st1 = Student(name='zheng12', age='123123', score=100)

st1.get_name()
st1.say_age()