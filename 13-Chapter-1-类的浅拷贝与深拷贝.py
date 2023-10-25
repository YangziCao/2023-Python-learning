'''
一. 变量的赋值操作
只是形成两个变量，实际上还是指向同一个对象

二. 浅拷贝
python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，因此，源对象与拷贝对象会引用同一个子对象

三. 深拷贝
使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同
##########################################
'''
#一.变量的赋值操作...
#0.00.0.0.0.0.0.0.