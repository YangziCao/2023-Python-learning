'''
循环结构
反复做同一件事情的情况，称为循环
循环的分类
1.while
2.for-in

语法结构
while 条件表达式：
   条件执行体（循环体）

选择结构的if与循环结构while的区别：
if时判断一次，条件为ture执行一次
while是判断N+1次，条件为ture执行N次
'''

a=1
#判断条件表达式
while a<10:
    #执行条件执行体
    print(a)  #输出1，2，3，4，5，6，7，8，9
    a+=1
'''
while循环的执行流程
四步循环法
1.初始变化量
2.条件判断
3.条件执行体（循环体）
4.改变变量
总结：初始化的变量与条件判断的变量与改变的变量为同一个
'''
#计算 0-4 之间的累加和
sum=0 #用于存储累加
#初始化变量 0
a=0
#条件判断
while a<5:
    #条件执行体（循环体） 累加和
    sum+=a
    #改变变量
    a+=1
print('和为',sum)  #print 需要在顶格，不然还在循环里面

'''
过程
a  a<5        sum   sum+=a
0  0<5  ture   0    0+0
1  1<5  ture   1    0+1
2  2<5  ture   3    1+2
3  3<5  ture   6    3+3
4  4<5  ture   10    6+4
5  5<5  flase
'''

#计算1-100之间的偶数和
sum=0
a=0
while a<101:
    sum+=a
    a+=2
print('和为',sum)

#h或者这样写
sum=0
a=0
while a<101:
    if a%2==0:
     sum+=a
    a+=1
print('和为',sum)

#或者
sum=0
a=0
while a<101:
    if not bool(a%2):
     sum+=a
    a+=1
print('和为',sum)

