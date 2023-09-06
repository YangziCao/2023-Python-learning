#本章内容
#1.程序的组织结构
#2.顺序结构
#3.对象的布尔值
#4.分支结构
#单分支if结构
#双分支if...else结构
#多分支if...elif...else结构
#if语句的嵌套
#条件表达式
#5.pass空语句

#1.程序的组织结构
#1996年，科学家证实了任何简单/复杂的算法都可以由顺序结构，选择结构和循环结构这三种基本结构组合而成

#2.顺序结构
#程序从上到下顺序地执行代码，中间没有任何的判断和跳转，直到程序结束

#3.对象的布尔值
#python一切皆对象，所有对象都有一个布尔值
#可使用内置函数bool（）获取对象的布尔值

#以下对象的布尔值为False
#Flase，数值0，None，空字符串，空列表，空元组，空字典，空集合
print(bool(False))  #false
print(bool(0))   #f
print(bool(0.0)) #f
print(bool(None)) #f
print(bool('')) #f
print(bool("")) #f
print(bool([])) #f 空列表
print(bool(list())) #f 空列表
print(bool(())) #f 空元组
print(bool(tuple())) #f 空元组
print(bool({})) #f 空字典
print(bool(dict())) #f 空字典
print(bool(set())) #f 空集合
#以上对象的布尔值为false ,其他对象的布尔值均为true
print(bool(18))
print(bool(True))
print(bool('hello world'))

#4.选择结构
#程序根据判断条件的布尔值选择性地执行部分代码，明确的让计算机知道在什么条件下，该去做什么