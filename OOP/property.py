# 属性监测


class Student(object):
  def get_s(self):
    return self.score

  def set_s(self, s):
    if not isinstance(s, int):
      raise ValueError('score must be an integer')
    if s < 0 or s > 100:
      raise ValueError('score must be 0~100')
    self.score = s

# 用raise语句来引发一个异常。异常/错误对象必须有一个名字，且它们应是Error或Exception类的子类。


s = Student()

# s.set_s(101) # ValueError: score must be 0~100
# s.set_s('123') # ValueError: score must be an integer

# 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，
# 负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作


class Man(object):
    @property
    def age(self):
      return self._age  # 记得下划线

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._age = value

m = Man()

m.age = 60

print(m.age)

# 定义只读属性， 之定义getter方法不定义setter方法
class Animal(object):
  @property
  def birth(self):
    return self._birth
  
  @birth.setter
  def birth(self, v):
    self._birth = v
  
  @property
  def age(self):
    return 1000
  
a1 = Animal()
# birth 是可读写属性
a1.birth = 'man'
print(a1.birth)
# age为只读属性
# a1.age = 1232321 AttributeError: can't set attribute
print(a1.age)