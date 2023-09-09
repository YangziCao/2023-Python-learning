#本章内容
#1.程序的组织结构
#2.顺序结构
#3.对象的布尔值
#4.分支结构
#单分支if结构
#(如果...就...)
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

#########################A. 单分支结构
'''

money=1000 #余额
s=int(input('请输入取款金额'))
#判断余额是否充足
if money>=s:
    money=money-s
    print('取款成功，余额为:',money)


###################B.双分支结构

#（如果...不满足...，就...） 二选一执行
#语法结构: if 条件表达式：
#条件执行体1
#else
#条件执行体2

    #从键盘录入一个整数，编写程序让计算机判断是奇数还是偶数
num=int(input('输入一个整数'))
#条件判断
if num%2==0:
    print(num,'是偶数')
else:
    print(num,'是奇数')


############C. 多分支结构（多选1去执行，多解决一个连续的区间段问题）

#中文语义
#成绩是在90分以上吗？ 不是
#成绩是在80分以上吗？不是
#成绩是在70分以上吗？不是
#成绩是在70分以下吗？是
#语法结构
#if 条件表达式1：
#条件执行体1
#elif 条件表达式2：   （elif  是else if 的缩写）
#条件执行体2
#elif条件表达式N：
#条件执行体N
#[else:]
#条件执行体N+1

#从键盘录入一个整数， 成绩
#90-100  A
#80-89   B
#70-79   C
#60-69   D
#0-59    E
#小于0/大于100为非法数据（不是成绩的有效范围

score=int(input('请输入一个成绩'))
if score>=90 and score<=100:
    print('A')
elif score>=80 and score<=89:
    print('B')
elif score>=70 and score<=79:
    print('C')
elif score>=60 and score<=69:
    print('D')
elif score>=0 and score<=59:
    print('D')
else:
    print('对不起，成绩有误，不在成绩的有效范围')

#python 中的简便写法

score=int(input('输入成绩'))
if 90<= score<=100:
    print('a')
elif 80<=score<=89:
    print('b')
elif 70<=score<=79:
    print('C')
elif 60<=score<=69:
    print('D')
elif 0<=score<=59:
    print('D')
else:
    print('对不起，成绩有误，不在成绩的有效范围')'''


######################D.嵌套if
#会员 >=200  8折
#    >=100  9折
#          不打折
#非会员 >=200  9.5折
#    以下    不打折
'''
answer=input('您是会员吗？y/n')
money=float(input('请输入您的购物金额:'))
if answer=='y':
 if money>=200:
    print('打8折，付款金额为:',money*0.8)
 elif money>=100:
    print('打9折，付款金额为:',money*0.9)
 else:
    print('不打折，付款金额为:',money)
else:
 if money>=200:
    print('打9.5折，付款金额为:',money*0.95)
 else:
    print('不打折，付款金额为:',money)
    
    '''


#######E.条件表达式
'''
条件表达式式if...else的简写
语法结构：
x if 判断条件 else y
运算规则：如果判断条件的bool值为True，条件表达式的返回值为x，否则条件表达式的返回值为Flase
'''
'''
从键盘录入两个整数，比较2个整数的大小'''

num_a=int(input('输入第一个整数'))
num_b=int(input('输入第二个整数'))
if num_a>=num_b:
    print(num_a,'大于等于',num_b)
else:
    print(num_a,'小于',num_b)

#简写上述代码   使用条件表达式进行比较
print((num_a,'大于等于',num_b) if num_a>=num_b else (num_a,'小于',num_b)) #这样写不好看，写成str类型

print(str(num_a)+'大于等于'+str(num_b) if num_a>=num_b else str(num_a)+'小于'+str(num_b))


#######F. pass语句
'''
pass语句其实什么都不做，只是一个占位符，用在语法上需要语句的地方
适用情况：先搭建语法结构，还没想好代码怎么写的时候
哪些语句一起使用 1.if语句的条件执行体，2.for-in语句的循环体，3.定义函数时的函数体
'''
if answer=='y':
    pass
else:
    pass
#如果没有想好具体的代码如何写，可以先写pass，这样就不会报错了