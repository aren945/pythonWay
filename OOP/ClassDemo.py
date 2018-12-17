# -*- coding: utf-8 -*-

class Student(object):
  pass


stu1 = Student()

stu1.name = 123

print(stu1)


# init方法
class Man():
  def __init__(self, name, score):
    self.name = name
    self.score = score
  def print_info(self): # 第一个参数一定是self, self表示实例本身
    print(self.name)

m1 = Man('zheng', 100)

print(m1.name)

#  私有属性
# 以__开头的属性或方法就私有属性方法 只允许class内使用

class MainMan():
  def __init__(self, name):
    self.__name = name
  def prinName(self):
    print(self.__name)


m2 = MainMan('哈哈')
m2.prinName()