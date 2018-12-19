import logging

def foo(s):
  return 10 / int(s)

def bar(s):
  return foo(s) * 2

def main():
  try:
    bar(0)
  except Exception as e:
    print('Error: %s' % e)
    logging.exception(e)
  finally:
    print('finally...')

main()

# 抛出错误

# class FooError(ValueError):
#   pass

# def foo1(s):
#   n = int(s)
#   if n == 0:
#     raise FooError('invalid value %s' % s)
#   return 10 / n

# foo1('0')


def foo3(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar3():
    try:
        foo3('0')
    except ValueError as e:
        print('ValueError!', e)
        raise

bar3()