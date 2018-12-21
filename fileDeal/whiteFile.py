# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
with open('./fileDeal/logger.log', 'a+', encoding="utf-8") as f1:
  print(f1.readlines())
  # f1.write('Hello Wrold！')