import functools


def d1(func):
    @functools.wraps(func)
    def wrapper():
        print('1234')
        print(func())
    return wrapper


@d1
def foo():
    print('this is function fun')
    return 'asd'


print(foo.__name__)
foo()

# --------------------------函数带参------------------------------


def d2(func):
    # @functools.wraps(func)
    def wrapper(*args, **kw):
        print('这是装饰器的打印')
        func(*args, **kw)
    return wrapper


@d2
def foo2(a, b):
    print('a is {0}, b is {1}'.format(a, b))


print('foo2 name %s' % foo2.__name__)

foo2(1, 2)


# ___________________________带参装饰器——————————————————————
def d3(text):
    def decorator(func):
        print('decirator print %s' % text)

        def wrapper(*args, **kw):
            print('wrapper print')
            return func(*args, **kw)
        return wrapper
    return decorator


@d3('test')
def foo3(a, b):
    print('a is %s , b is %s' % (a, b))


foo3(3, 4)

# ---------------------类装饰器------------------------


class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('class decorator runing')
        self._func()
        print('class decorator ending')


@Foo
def bar():
    print('bar')


bar()
# ------------------------装饰器顺序-------------------


def d4(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('this is decorator4')
        return func(*args, **kw)
    return wrapper


def d5(text):
    def decorator(func):
        print('log is %s' % text)

        def wrapper(*args, **kw):
            print('asd')
            return func(*args, **kw)
        return wrapper
    return decorator


@d4
@d5('多个装饰器')
def foo4(a, b):
    print('a is %s, b is %s' % (a, b))


foo4(10, 20)

if (False, False):
  print(123213)