'''
列表元素的增加操作
1.append()   在列表的末尾添加一个元素
2.extend（）  在列表的末尾至少添加一个元素
3.insert（）  在列表的任意位置添加一个元素
4.切片        在列表的任意位置添加至少一个元素
'''

#1.
lst=[10,20,30]
print(lst,id(lst))
#[10, 20, 30] 1715100996672

lst.append(100)
print(lst,id(lst))
#[10, 20, 30, 100] 1715100996672
#2个列表的ID未改变，说明未创建新的列表对象。

lst2=['hello','world']
lst.append(lst2)
print(lst)
#[10, 20, 30, 100, ['hello', 'world']]
#将lst2作为一个元素添加到列表的末尾

#2.
lst1=[10,20,30]
lst2=['hello','world']
lst1.extend(lst2)
print(lst1)
#[10, 20, 30, 'hello', 'world']
#是在lst1的列表末尾扩展。 比较line22 and 30

#3.insert
#在任意位置上添加
lst1.insert(1,90)  #在索引为1的地方添加90
print(lst1)
#[10, 90, 20, 30, 'hello', 'world']

#4.切片
lst3=['true','false','hello']
#在任意的位置添加N多个元素
lst[1:]=lst3   #在原lst列表索引为1的地方开始切，然后把lst3放进去。 替换
print(lst)
#[10, 'true', 'false', 'hello']