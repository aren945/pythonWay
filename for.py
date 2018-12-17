import os
l = [x * x for x in range(1, 10) if x % 2 == 0]
# o = {x for x in range(1, 10) }

print(l)


print([d for d in os.listdir('../')])

L = ['Hello', 'World', 18, 'Apple', None]

print([x.lower() for x in L if isinstance(x, str)])
