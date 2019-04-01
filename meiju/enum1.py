from enum import Enum, IntEnum


class VIP(Enum):
	yellow = 1
	green = 2
	red = 3
	black = 4


print(VIP.black)  # VIP.black
print(VIP.black.value)  # 4
print(VIP.black.name)  # black
'''
枚举和普通类相比有什么优势：

1.字典或者Class 都是可更改的
2.有可能存在相同的key




'''


# 枚举遍历
for v in VIP:
	print(v)

# 枚举的比较运算, 只支持等值比较， 不支持大小比较

print(VIP.black == VIP.green) # False
print(VIP.black == 4) # False
print(VIP.black.value == 4) # True


class TESTENUM(IntEnum):
	pass
