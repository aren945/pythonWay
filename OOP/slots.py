# slots 限制添加类的属性
class Student(object):
  __slots__ = ('name', 'age') #定义允许绑定的属性名称
  pass
  def pin(self):
    pass

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
s = Student()

s.name = '123'
s.age = 12

# s.score = 123 报错

# print(s.__dict__) 定义了slots就没了dict
