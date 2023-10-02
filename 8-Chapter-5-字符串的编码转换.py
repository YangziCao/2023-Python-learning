'''
字符串的编码转换
一.为什么需要字符串的编码转换
A计算机（str在内存中以Unicode表示）→编码→byte字节输出→解码→显示在B计算机中

二.编码与解码的方式
编码：将字符串转换位二进制数据（bytes）
解码：将bytes类型的数据转换成字符串类型
'''
s='天涯共此时'
#编码
print(s.encode(encoding='GBK'))   #在GBK编码格式中，一个中文占两个字节
#b'\xcc\xec\xd1\xc4\xb9\xb2\xb4\xcb\xca\xb1'
#b表示byte，二进制
print(s.encode(encoding='UTF-8')) #在UTF-8编码格式中，一个中文占三个字节
#b'\xe5\xa4\xa9\xe6\xb6\xaf\xe5\x85\xb1\xe6\xad\xa4\xe6\x97\xb6'

#解码
#byte代表的就是一个二进制数据/字节类型的数据
byte=s.encode(encoding='GBK')  #编码
print(byte.decode(encoding='GBK')) #解码
#天涯共此时

byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))
#天涯共此时