# 实例属性优先级高于类属性

class Student(object):
  name = 'zheng'
  def __init__(self):
    self.n = '123'

print(Student.name)

a = Student()
b = Student()

print('___________________________________')

print(a.name)
print(b.name)

a.name = 'Xinglun'

print('___________________________________')

print(a.name)
print(b.name)
