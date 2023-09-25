'''
字典是一个无序的序列，以键值对的方式存储数据
'''

'''
一. 字典的创建
最常用的方式：
1.使用花括号
2.使用内置函数
'''
#1.花括号
scores={'zhangsan':100,'lisi':98}
print(scores)
print(type(scores))
#  {'zhangsan': 100, 'lisi': 98}
#  <class 'dict'>

#2.使用内置函数，dict（）
student=dict(name='jack',age=20)   #jack是字符串要加’‘
print(student)
#{'name': 'jack', 'age': 20}

#3.创建空字典
d={}
print(d)

'''
二. 字典中元素的获取
1.[]         举例：scores[‘zhangsan’]
2.get()方法  举例：scores.get（‘zhangsan’）

二者的区别
a. []如果字典中不存在指定的key，抛出keyError异常
b.get（）方法取值，如果字典中不存在指定的key，并不会抛出keyError而是返回None，可以通过参数设置默认的Value，以便指定的KEY不存在时返回'''

#第一种方式
scores={'zhangsan':100,'lisi':98}
print(scores['zhangsan'])
#100

#第二种方式
print(scores.get('zhangsan'))
#100
print(scores.get('wangwu'))
#None
print(scores.get('chenliu',99))
#99 是在查找chenliu所对应的value不存在时，提供的默认值

'''
三. key的判断
1. in👉指定的key在字典中存在,返回True👉’zhangsan‘ in scores
2. not in 👉指定的key在字典中不存在,返回True👉’Many‘ not in scores
'''

scores={'zhangsan':100,'lisi':98}
print('zhangsan' in scores) #True
print('zhangsan' not in scores) #False


'''
四.字典元素的删除
'''
#1.删除指定的键值对，key-value   一删删一对
del scores['zhangsan']
print(scores)
#{'lisi': 98}

#2.清空字典的元素
scores.clear()
print(scores)
#{}

'''
五.字典元素的新增
'''
scores1={'zhangsan':100,'lisi':98}
scores1['jack']=90
print(scores1)
#{'zhangsan': 100, 'lisi': 98, 'jack': 90}
#删除和新增使用中括号

'''
六. 修改元素
'''
#将jack 98 改为100
scores1['jack']=100
print(scores1)
#{'zhangsan': 100, 'lisi': 98, 'jack': 100}


'''
七.获取字典视图的三个方法
1. key（）👉获取字典中所有的key
2. values（）👉获取字典中所有的value
3. items（）👉获取字典中所有的key.value对
'''
#1.获取所有的key
scores={'zhangsan':100,'lisi':98,'wangwu':45}
keys=scores.keys()
print(keys)
print(type(keys))
#dict_keys(['zhangsan', 'lisi', 'wangwu'])
#<class 'dict_keys'>
print(list(keys))  #将所有的key组成的视图转成列表
#['zhangsan', 'lisi', 'wangwu']

#2.获取所有的value
values=scores.values()
print(values)
print(type(values))
#dict_values([100, 98, 45])
#<class 'dict_values'>
print(list(values))  #转换为列表
#[100, 98, 45]

#3.获取所有的键值对
items=scores.items()
print(items)
print(type(items))
print(list(items)) #转换后的列表元素是由元组组成
#dict_items([('zhangsan', 100), ('lisi', 98), ('wangwu', 45)])
#<class 'dict_items'>
#[('zhangsan', 100), ('lisi', 98), ('wangwu', 45)]

'''
八.字典元素的遍历
'''
# for item in scores:
#     print(item)
scores={'zhangsan':100,'lisi':98,'wangwu':45}
for item in scores:
    print(item)
#zhangsan
#lisi
#wangwu
#输出的是所有的key

#如果想输出字典当中的值的话，有2种方法
for item in scores:
    print(item,scores[item])
    print(item,scores.get(item))

'''
九.字典的特点
1.字典中的所有元素都是一个key-value对，key不允许重复，value则可以
2.字典种的元素是无序的（列表可以在索引的地方插入指定原，但是字典是不可以的）
3.字典中的key必须是不可变对象 （不可变对象有整数，字符串。 而列表是可变对象，用lst去做key的话是不可以的）
4.字典也可以根据需要动态地伸缩
5.字典会浪费较大的内存，是一种使用空间换时间的数据结构
'''
#1.key不允许重复，value则可以
d={'name':'zhangsan','name':'lisi'}
print(d)
#{'name': 'lisi'}
#后面的lisi覆盖了前面的zhangsan

d={'name':'zhangsan','nikename':'zhangsan'}
print(d)
#{'name': 'zhangsan', 'nikename': 'zhangsan'}
#value可以重复

'''
十.字典生产式
items=['Fruits','Books','Others']
prices=[96,78,85]
将上面的整合为
{‘Fruits’：96，‘Books’：78，‘Others’：85}

内置函数zip（）
用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组组成的列表
'''

items=['Fruits','Books','Others']
prices=[96,78,85]

d={item:price for item,price in zip(items,prices)}
print(d)
#{'Fruits': 96, 'Books': 78, 'Others': 85}

#如果key需要大写的话，则
d={item.upper():price for item,price in zip(items,prices)}
print(d)
#{'FRUITS': 96, 'BOOKS': 78, 'OTHERS': 85}

items=['Fruits','Books','Others']
prices=[96,78,85,100,120]

d={item:price for item,price in zip(items,prices)}
print(d)
#{'Fruits': 96, 'Books': 78, 'Others': 85}
#如果元素数量不统一，  打包的过程中，以元素少的为基准进行生成。