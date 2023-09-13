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


'''
2. for-in循环
in表达从（字符串，序列等）中依次取值，又称为遍历
for-in遍历的对象必须是可迭代对象
语法结构
for 自定义的变量 in 可迭代对象：
循环体
循环体内不需要访问自定义变量，可以将自定义变量替代为下划线
'''
for item in'python':
    print(item)
#指在python这个字符串里面，依次将python取出，赋给item，第一次取出来的是P，将p赋值给item，将item的只输出
'''
输出结果
p
y
t
h
o
n
'''
#range（）是一个整数序列，也是一个可迭代对象
for i in range(10):#range（10）指产生0-9的整数序列，步长为1
    print(i)
'''
output
0
1
2
3
4
5
6
7
8
9
'''

#如果在循环体中不需要使用到自定义变量，可将自定义变量写为”_“
for _ in range(5):
    print('人生苦短，我用python')
'''
输出结果：
人生苦短，我用python
人生苦短，我用python
人生苦短，我用python
人生苦短，我用python
人生苦短，我用python
    '''

#使用FOR循环计算1-100之间的偶数和
sum=0 #用于存储偶数和
for item in range(1,101):
    if item %2==0:
        sum+=item
print('1-100之间的偶数和为：',sum)

#输出：1-100之间的偶数和为： 2550

#题目要求：输出100-999之间的水仙花数
#水仙花数：各位的数的3次方+十位数的3次方+百位数的三次方之和=这个数
#153=3*3*3+5*5*5+1*1*1
for item in range(100,1000):
    ge=item%10         #各位上的数
    shi=item//10%10    #十位上的数
    bai=item//100      #百位上的数
  #  print(bai,shi,ge)
    if ge**3+shi**3+bai**3==item:
        print(item)
#输出结果
'''
153
370
371
407
'''
