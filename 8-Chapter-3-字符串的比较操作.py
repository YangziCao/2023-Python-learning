'''
字符串的比较操作
1.运算符：>, >=, <, <=, ==, !=
2.比较规则
首先比较两个字符串中的第一个字符，如果相等则继续比较下一个字符，依次比较下去，直到两个字符串中的字符不相等时，其比较结果就是两个字符串的比较结果，
两个字符串中的所有后续字符将不再被比较
3.比较原理
两个字符进行比较时，比较的是其ordinal value（原始值），调用内置函数ord可以得到指定字符的ordinal value。与内置函数ord对应的是内置函数chr，
调用内置函数chr时指定ordinal value可以得到其对应的字符
'''
print('apple'>'app')  # True

print('apple'>'banana') # False
#两个字符串进行比较时，比较的是其ordinal value
print(ord('a'),ord('b')) # 97 98
# 97>98  所以是false

print(chr(97),chr(98))  # a b

print(ord('曹'))
#26361
print(chr(26361))
#曹

'''
== 与is的区别
==比较的是 value
is比较的是 id是否相等
'''

a=b='python'
c='python'
print(a==b) #True
print(b==c) #True
print(a is b) #True
print(a is c) #True
print(id(a))  #2082832140592
print(id(b))  #2082832140592
print(id(c))  #2082832140592
#字符串驻留机制