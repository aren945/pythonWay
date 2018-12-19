try:
  f = open('logger.log', 'r')
  print(f.read())
finally:
  if f:
    f.close()


with open('logger.log', 'r') as f1:
  print(f1.read())