from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# value属性则是自动赋给成员的int常量，默认从1开始计数
for name, member in Month.__members__.items():
  print(name, '=>', member, ',', member.value)


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum, unique

@unique
class Weekday(Enum):
  Sun = 0 # Sun的value被设定为0
  Mon = 1
  Tue = 2
  Wed = 3
  Thu = 4
  Fri = 5
  Sat = 6

day1 = Weekday.Mon
print(day1)

day2 = Weekday.Mon.value
print(day2)

print(Weekday(3))

list1 = [1,2,3,1,4,5,6,7,3,2,4]

print(tuple(list1))
print(set(list1))