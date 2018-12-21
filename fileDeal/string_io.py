from io import StringIO
# StringIO顾名思义就是在内存中读写str。
# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：

f = StringIO()
f.write('hello')

print(f.getvalue())