import os
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.name)
# print(os.uname()) # win没有这个方法
# os.uname_result()


import platform

print(os.environ)
print(platform.uname())