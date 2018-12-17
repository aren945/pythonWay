a = 'abced'
print(a.capitalize())

c,d, e = [1,2,3]
c = c+ 1

def createCounter():
    g = 0
    def counter():
        # 只能引用外部变量值，不能修改、
        nonlocal g
        g = g + 1
        print(g)
        return a 
    return counter


createCounter()()
print(c)