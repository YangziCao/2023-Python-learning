'''
集合是可变序列，所以可以增删改

一.集合元素的判断操作
in 或 not in

二.集合元素的新增操作
1.调用add（）方法，一次添中一个元素
2.调用update（）方法，至少添中一个元素

三.集合元素的删除操作
1.调用remove（）方法，一次删除一个指定元素，如果指定的元素不存在，则抛出KeyError
2.调用discard（）方法，一次删除一个指定元素，如果指定的元素不存在，不抛出异常
3.调用pop（）方法，一次只删除一个任意元素  （删除任意元素，随机一个, 不可以指定具体参数，否则抛异常）
4.调用clear（）方法，清空集合
'''

# 一. 判断操作
s={10,20,30,405,60}
print(10 in s) #True
print(10 not in s) #False

# 二. 新增操作
# 1. 一次添加一个元素
s.add(80)
print(s)
#{80, 20, 405, 10, 60, 30}

# 2. 一次至少添加一个元素
s.update({200,400,300})
print(s)
#{200, 10, 300, 80, 400, 20, 405, 60, 30}  #将一个集合添加到指定的集合当中

s.update([100,99,8])  #将列表放入集合
s.update((78,64,55))  #将元组放入集合
print(s)
#{64, 99, 100, 200, 8, 10, 300, 78, 80, 400, 20, 405, 55, 60, 30}

# 三. 删除操作
# 1.
s.remove(100)
print(s)
# {64, 99, 200, 8, 10, 300, 78, 80, 400, 20, 405, 55, 60, 30}

# 2.
s.discard(500)  #不存在此元素的话，也不会报错，优于remove方法
s.discard(300)
#{64, 99, 200, 8, 10, 300, 78, 80, 400, 20, 405, 55, 60, 30}

# 3. pop()  删除任意元素，随机一个, 不可以指定具体参数，否则抛异常
s.pop()
print(s)
# {99, 200, 8, 10, 78, 80, 400, 20, 405, 55, 60, 30}
s.pop()
print(s)
#{200, 8, 10, 78, 80, 400, 20, 405, 55, 60, 30}

# 4.
s.clear()
print(s)
# set()