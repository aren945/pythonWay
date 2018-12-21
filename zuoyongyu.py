x = 1 

def foo():
    x = 2 
    def innerfoo():
      # x = 3 
      print('locals ', x)
    innerfoo()
    print('enclosing function locals ', x)
foo()
print('global ', x)