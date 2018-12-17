def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。


@log
def now():
    print('123123')

print(now.__name__) # wrapper
now()


#  带参装饰器

def log1(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 先执行log1， 返回一个decorator方法，然后调用decorator，传入的参数是fun2， 最终返回wrapper方法.
@log1('execute')
def fun2():
  print('func2')
# 由于相当于执行的的是wrapper方法，所fun2.__name__是wrapper
print(fun2.__name__) # wrapper

fun2()

## 修正__name__
import functools
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 先执行log1， 返回一个decorator方法，然后调用decorator，传入的参数是fun2， 最终返回wrapper方法.
@log2('execute')
def fun3():
  print('func3')
# 由于相当于执行的的是wrapper方法，所fun2.__name__是wrapper
print(fun3.__name__) # wrapper

fun3()