'''
           名称              描述
特殊属性   __dict__   获得类对象或实例对象所绑定的所有属性和方法的字典
特殊方法   _len__()  通过重写_len_()方法，让内置函数len()的参数可以是自定义类型
         __add__()  通过重写_add_()方法，可使用自定义对象具有“+”功能
         __new__()  用于创建对象
        __init__()  对创建的对象进行初始化
'''

#1. __dict__ 绑定属性
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
#创建C类的对象
x=C('Jack',20)  #x是C类型的实例对象
print(x. __dict__)   #实例对象的属性字典
#{'name': 'Jack', 'age': 20}
print(x.__class__)
#<class '__main__.C'>   输出了对象所属的类
print(C.__bases__)
#(<class '__main__.A'>, <class '__main__.B'>)         输出了C类的父类类型的元素
print(C.__base__)
#<class '__main__.A'>   line15中，A and B，谁写在前面，就先输出谁
print(C.__mro__)
#(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
#查看c的层次结构

print(A.__subclasses__())
#[<class '__main__.C'>]   查看A的子类


#2.__len__ /__add__
a=20
b=100
c=a+b  #2个整数类型的对象的相加操作
d=a.__add__(b)

print(c)  #120
print(d)  #120

#class Student:
#    def __init__(self,name):
#        self.name=name
#
#stu1=Student('ZHANGSAN')
#stu2=Student('lisi')
#s=stu1+stu2
#print(s)
#这样add会报错,因为是字符串类型 如果非要add，可以如下
class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name

stu1=Student('ZHANGSAN')
stu2=Student('lisi')
s=stu1+stu2
print(s)
#ZHANGSANlisi
#实现了2个对象的加法运算（因为在Student类中 编写__add__（）特殊方法）

lst=[11,22,33,44]
print(len(lst))    #此处len是内置函数len
#4
print(lst.__len__())
#4


#
class Person():  #不写默认object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __new__(cls, *args, **kwargs):
        ##################
