'''
面对对象的三大特征
一.封装： 提高程序的安全性
a. 将数据（属性）和行为（方法）包装到类对象中。在方法内部对属性进行操作，在类对象的外部调用方法。这样，无需关心方法内部的具体实现细节，从而隔离了复杂度
b. 在Python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，前边使用两个 下划线，  “_”

二.继承： 提高代码的复用性
三.多态： 提高程序的可扩展性和可维护性
'''

#一. 封装
#a.
class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已启动')

car=Car('宝马X5')
car.start()
print(car.brand)
#汽车已启动
#宝马X5

#b.
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age  #年龄不希望在类的外部被使用，所以加了两个 __  ,但是可以在内部被使用
    def show(self):
        print(self.name,self.__age)
#Jack 20
stu=Student('Jack',20)
stu.show()
#在类的外部使用name与age
print(stu.name)
#Jack

#print(stu.__age)
#报错  AttributeError: 'Student' object has no attribute '__age'

#那么如何在外部获取呢
print(dir(stu))
#['_Student__age', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'show']
#发现第一个有age
#调用
print(stu._Student__age)
#20
#在类的外部可以通过  _Student__age进行访问

'''
二.继承
1.语法格式
class 子类类名（ 父类1，父类2...）
      pass
如果一个类没有继承任何类，则默认继承object

Python支持多继承，父类里面可继承多个
定义子类时，必须在其构造函数中调用父类的构造函数
'''
#2.继承的代码实现
class Person(object):  #Person继承object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no

class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear

stu=Student('Mells',20,'1001')
teacher=Teacher('Nakho',34,10)

stu.info()
teacher.info()


#多继承实例   Python支持多继承，父类里面可继承多个
class A(object):
    pass

class B(object):
    pass

class C(A,B):
    pass
#c类同时继承A和B，  AB是c的父类


#3.方法重写
#如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其（方法体）进行重新编写
#子类重写后的方法中可以通过super（）.xxx()调用父类中被重写的方法

