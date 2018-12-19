class Animal(object):
  def say(self):
    print('this is Animal')

class FlyAnimal(object):
  def say(self):
    print('this is FlyAnimal')

# 多继承 同名方法 取靠前的
class Bird(FlyAnimal, Animal):
  pass
  
a = Bird()

a.say()

