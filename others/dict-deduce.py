students = {
	'stu1': 12,
	'stu2': 23,
	'stu3': 32
}

b = {key: val for key, val in students.items()}
c = (key for key, val in students.items())

print(b)

for i in c:
	print(i)
