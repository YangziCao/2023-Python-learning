'''
一.什么是元组
1.元组
python内置的数据结构之一，是一个不可变序列


2.不可变序列与可变序列
a. 不变可变序：字符串，元组
不变可变序列：没有增删改的操作

b. 可变序列：列表，字典
可变序列：可以对序列执行增删改操作，对象地址不发生更改
'''

# 可变序列  列表
lst=[10,20,45]
print(id(lst))
lst.append(300)
print(id(lst))
#2470982997056
#2470982997056
#地址不变

#不可变序列  字符串 元组     没有增删改操作
s='hello'
print(id(s))
#2636599153008
s=s+'world'
print(id(s))
#2636599153136
print(s)
#helloworld

'''
二.元组的创建方式
'''
#1.直接小括号
t=('python','hello',90)
print(t)
print(type(t))
#('python', 'hello', 90)
#<class 'tuple'>

t2='python','hello',90   #小括号可以省略
print(t2)
print(type(t2))
#('python', 'hello', 90)
#<class 'tuple'>


#2.使用内置函数
t1=tuple(('python','hello',92))


#3.只包含一个元组的元素需要使用逗号和小括号
#如果不加逗号的话，会识别为一个它本身的数据类型，而不是元组
t3=(10,)
print(t3)  #(10,)
print(type(t3))
#<class 'tuple'>

t4=('python')
print(type(t4))
#<class 'str'>

t5=(10)
print(type(t5))
#<class 'int'>

#4. 空元组的创建方式
t6=()
t7=tuple()
print(t6,t7)
#() ()

#空列表的常见方式
lst=[]
lst1=list()
print(lst,lst1)
#[] []

#空字典的创建方式
d={}
d2=dict()
print(d,d2)
#{} {}




'''
三. 为什么要将元组设计成不可变序列
因为在多任务环境下，同时操作对象时不需要加锁
因此，在程序中尽量使用不可变序列

注意事项：元组中存储的是对象的引用
a. 如果元组中对象本身不可对象，则不能再引用其他对象
b. 如果元组中的对象是可变对象，则可变对象的引用不允许改变，但数据可以改变
'''