# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态
# python -m pdb
import pdb
s = '0'
n = int(s)

pdb.set_trace()

print(10 / n)