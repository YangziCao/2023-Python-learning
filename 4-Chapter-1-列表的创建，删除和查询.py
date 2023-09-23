a=10 #变量存储的是一个对象的引用
lst=['hello','world','98']
print(id(lst))
print(type(lst))
print(lst)
'''
2377895859264
<class 'list'>
['hello', 'world', '98']
'''

#创建列表的第一种方式，使用[]
lst=['hello','world','98']

#创建列表的第二种方式，使用内置函数list（）
lst2=list(['hello','world','98'])


'''
列表的特点
1.列表元素按顺序有序排序
2.索引映射唯一数据，索引正向从0开始，   负数的话从-1开始，最后一个是-1，一次往前数-2，-3    比如上面的hello索引可以是0也可以是-3
3.列表可以存储重复数据
4.任意数据类型可以混存
5.根据需要动态分配和回收内存 
'''
#解释第二特点的第二条
lst=['hello','world','98']
print(lst[0],lst[-3])
#hello hello, 结果输出都是hello

'''
列表的查询操作
1.获取列表中指定元素的索引
index（）
a.如查列表中存在N个相同元素，只返回相同元素中的第一个元素的索引
b.如果查询的元素在列表中不存在，则会抛出ValueError
c.还可以在指定的start和stop之间进行查找

2.获取列表中的单个元素
a.正向索引从0到N-1，举例lst[0]
b.逆向索引从-N到-1，举例lst[-N]
c.指定索引不存，抛出IndexError

'''


'''
lst=['hello','world','98','hello']
print(lst.index('hello'))
#output  0
#如果列表中存在相同元素，只返回相同元素中的第一个元素的索引
print(lst.index('python'))

#ValueError: 'python' is not in list

print(lst.index('hello,1,3'))
#ValueError: 'hello,1,3' is not in list
# 1,3  在1-3的位置上查找hello，报错   索引为1的是world，2是98，3是hello，  但是不包括3，只从1和2中查找
#改为1，4就可以查到

'''

lst=['hello','world',98,'hello',234]
#获取索引为2的元素
print(lst[2])
print(lst[-3])
#都是98

#列表元素的查询操作-
# 3.获取列表中的多个元素
lst=[10,20,30,40,50,60,70,80]
#start=1,stop=6,step1
print(lst[1:6:1])
#[20, 30, 40, 50, 60]    #不包括6    切片的范围左闭右开
print('原列表',id(lst))
#原列表 2242044646464

lst2=lst[1:6:1]
print('切的片',id(lst2))
#切的片 2242045443008
#所以新切出来的片，是一个新的列表

print(lst[1:6])
#[20, 30, 40, 50, 60],和之前那个一样，不写步长的话，默认步长为1

print(lst[1:6:])
#[20, 30, 40, 50, 60], 冒号后面不写，也默认步长为1

#start=1 stop=6 step=2
print(lst[1:6:2])
#[20, 40, 60]

#若不写start，则默认为1
# stop=6 step=2 start默认
print(lst[:6:2])
#[10, 30, 50]

#start=1 step=2,stop默认
print(lst[1::2])
#[20, 40, 60, 80]  默认到最后一个元素

#step步长为负数的情况
print(lst[::-1])  #默认start 和stop
#[80, 70, 60, 50, 40, 30, 20, 10]
#第一个元素是原列表的最后一个元素

print(lst[7::-1])
#[80, 70, 60, 50, 40, 30, 20, 10]

print(lst[6:0:-2])
#[70, 50, 30]   到0结束，但是不包含0，  start 是闭区间，stop是闭区间

'''
列表元素的查询操作
1.判断指定元素在列表中是否存在
元素 in 列表名
元素 not in 列表名
2.列表元素的遍历
for 迭代变量 in 列表名
操作

'''
#1.
print('p' in 'python')  #true
print('k' not in 'python') #true

lst=[10,20,'python','hello']
print(10 in lst) #true

#2.列表元素的遍历
for item in lst:
    print(item)
'''
输出
10
20
python
hello
'''