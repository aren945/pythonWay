
import  re

a = 'c|c++|python'

r = re.findall('python', a)
print(r)


b = 'C09012JDKANS}|{}>?<lkl132'

# r1 = re.findall('(?=\d{2}\B)', b)
r2 = re.findall('\d{2}', b)
# print(r1)
print(r2)


c = 'abc, acc, adc, aec, afc, ahc'

print(re.findall('a[^bcf]c', c))
print(re.findall('a[e-h]c', c))

# 概括字符集
d = 'javascriptdjk12321a1231'
# \d 数字 \D 非数字 \w 匹配字母、数字、下划线。等价于'[A-Za-z0-9_]'。 \s 空白字符

e = '<script>alert(123);</script>'
r12 = re.search('<script>([\s\S]*?)</script>', e)
# 返回括号里的
print(r12.group(1))

# 贪婪和非贪婪

# 替换
#
# f = '<script>alert(123);</script>'
#
# def covert(value):
# 	print(value.group())
#
# # f1 = re.sub('<script>([\s\S]*?)</script>', 'console.log(1)', f)
#
# f1 = re.sub('<script>([\s\S]*?)</script>', covert, f)
#
# print(f1)