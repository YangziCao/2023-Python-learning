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