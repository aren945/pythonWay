'''
列表推导式
list set 元组能被推导
'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

b = [i * i for i in a if i >= 3]  # 列表推导式

print(b)