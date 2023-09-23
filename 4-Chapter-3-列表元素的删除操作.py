'''
列表元素的删除操作
一. remove（）
1.一次删除一个元素
2.重复元素只删除第一个
3.元素不存在抛出ValueError

二. pop()
1.删除一个指定索引位置上的元素
2.指定索引不存在抛出IndexError
3.不指定索引，删除列表中的最后一个元素

三. 切片
一次至少删除一个元素

四. clear（）
清空列表

五. del
删除列表
'''

# 一.
lst=[10,20,30,40,50,60,30]
lst.remove(30)
print(lst)
#[10, 20, 40, 50, 60, 30]
#从列表中移除一个元素，如果有重复元素只移除第一个元素，  3个重复的，就remove2次。

# 二. pop()
lst.pop(1)   #删除索引位置为1的元素
print(lst)
#[10, 40, 50, 60, 30]

lst.pop()   #不写索引位置的话，默认删除列表中的最后一个元素
print(lst)
#[10, 40, 50, 60]

# 三. 切片：一次至少删除一个元素
#但是切片会产生一个新的列表对象
new_list=lst[1:3]
print(lst)
#[10, 40, 50, 60]
print(new_list)
#[40, 50]   取出来

#如何不产生新的列表对象，而是删除原列表中的内容
lst[1:3]=[]   #取不到3，stop是开区间
print(lst)
#[10, 60]
#相当于把索引位置为1和2的元素取出来到空列表。

# 四. clear()  清除列表中的所有元素
lst.clear()
print(lst)
#[]   输出空列表

# 五. del  删除列表
del lst
print(lst)
#NameError: name 'lst' is not defined. Did you mean: 'list'?  lst已被删除