# 使用type()
# 判断对象类型，使用type
type(12)

import ClassDemo

a = ClassDemo.Man('zheng', 100)

print(type(123))
print(type(a))


import types

def fn():
  pass

print(type(fn))

# 判断是否是函数
print(type(fn) == types.FunctionType)

print(type(x for x in range(10)) == types.GeneratorType)

# 判断继承关系

print (isinstance(a, ClassDemo.Man))
print (isinstance(a, object))
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
print(dir('ABC'))
print(dir(ClassDemo))
# len方法实质上在len方法内部，他自动去调用该对象的__len__()方法，如果我们自己写的类也想用len()方法，就自己写一个__len__()方法

class MyDog(object):
  def __len__(self):
    return 100
    
dog = MyDog()

print(len(dog))
