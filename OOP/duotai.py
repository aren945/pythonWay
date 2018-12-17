# -*- conding:utf-8 -*-

class Man():
  def __init__(self, name):
    self.name = name
  def printInfo(self):
    print(self.name)

class genMan(Man):
  # def __init__(self):
    # self.__gender = 'man'
  def printInfo(self, otherInfo):
    print(self.name)
    print('this is otherInfo')

g1 = genMan('dasd ')
g1.printInfo('dasd')

print('g1 name is %s' % g1.name)

print((lambda x: x+1)(2))