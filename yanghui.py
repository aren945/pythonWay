
def san(max):
  n, p, no = 0, [1], [1]
  while n < max:
    yield no
    p = no
    if n < 1:
      no.append(1)
    else:
      for index, x in enumerate(p):
        pass
        if (index == 0):
          no = [1]
        else:
          no.append(p[index] + p[index-1])
      no.append(1)
    n += 1
  return 'done'

for x in san(5):
  print(x)

import sys
print(dir(sys))