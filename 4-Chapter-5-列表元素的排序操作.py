'''
列表元素的排序操作
常见的两种方式
1.调用sort（）方法，列表中的所有元素默认按照从小到大的顺序进行排序，可以指定 reverse=True,进行降序排序    (对原列表)
2.调用内置函数sorted（），可以指定reverse=True，进行降序排序，原列表不发生改变     （产生一个新的列表）
'''

#1.
lst=[20,40,10,98,54]
#开始排序，调用列表对象的sort方法，升序排序
lst.sort()
print(lst)
#[10, 20, 40, 54, 98]

#通过指定关键字参数，将列表中的元素进行降序排序
lst.sort(reverse=True) #reverse = true 表示降序排序， reverse= false 就是升序排序
print(lst)
#[98, 54, 40, 20, 10]

lst.sort(reverse=False)
print(lst)
#[10, 20, 40, 54, 98]

#2. 使用内置函数 sorted（）进行排序
lst=[20,40,10,98,54]
#开始排序
new_list=sorted(lst)
print(new_list)
#[10, 20, 40, 54, 98]

#指定关键字参数，进行降序排序
desc_list=sorted(lst,reverse=True)
print(desc_list)
#[98, 54, 40, 20, 10]