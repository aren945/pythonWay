list_x = [1,2,3,4,5,6,7]


def square(x):
	print(x)
	return x * x

r = map(square, list_x)

print(list(r))