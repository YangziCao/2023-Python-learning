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
#Mells 20
#Nakho 34


#多继承实例   Python支持多继承，父类里面可继承多个
class A(object):
    pass

class B(object):
    pass

class C(A,B):
    pass
#c类同时继承A和B，  AB是c的父类



#--------------------------------------------------------------------------------------------------
#3.方法重写
#如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其（方法体）进行重新编写
#子类重写后的方法中可以通过super（）.xxx()调用父类中被重写的方法

#EX. line62-85  无法输出学号和教龄， 但是info的方法完不成这个操作 因为父类中既没有学号no也没有教龄 teachofyear
#此时子类想输出自己的东西，父类已经无法满足需求了
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
    def info(self):  #此时左边出现一个箭头，鼠标放上去显示 overrides method in Person(覆盖person中的方法)
        super().info()   #不写此行的话，只会打印出，学号，而不会打印出之前的name and age
        print(self.stu_no)

class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear
    def info(self):
        super().info()
        print('教龄',self.teachofyear)

stu=Student('Mells',20,'1001')
teacher=Teacher('Nakho',34,10)

stu.info()
teacher.info()
#Mells 20
#1001
#Nakho 34
#教龄 10



#---------------------------------------------------------------------------------------------------------
#4.object类
'''
object类是所有类的父类，因此所有类都有object类的属性和方法     
如果一个类没有继承任何类，则默认继承object
内置函数dir()可以查看指定对象所有属性
object有一个 _str_()方法，用于返回一个对于“对象的描述”，对应于内置函数str()经常用于print()方法，帮助我们查看对象的信息，所以我们经常会对
_str_()进行重写
'''
class Student:
    pass
stu=Student()
print(dir(stu))  #查看stu这个类所具有的属性和方法
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
# print如此多的属性和方法不是我们在student类里所定义的，这些属性和方法都是从父类object当中所继承过来的
print(stu)
#<__main__.Student object at 0x000001DD574143D0>  查看地址

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return'我的名字是{0}，今年{1}岁'.format(self.name,self.age)

stu=Student('Jack',20)
print(dir(stu))
print(stu)   #默认调用str方法
#我的名字是Jack，今年20岁
#重写了str之后，不再输出对象的内存地址，而是调用str函数，输出里面的内容
print(type(stu))
#<class '__main__.Student'>

'''
三. 多态
简单地说，多态就是“具有多种形态”，它指的是：即使不知道一个变量所引用的对象到底是什么类型，仍然可以通过这个变量调用方法，
在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法
'''
class Animal(object):
    def eat(self):
        print('动物会吃')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

class Person:   #没有继承任何类，则默认继承object类
    def eat(self):
        print('人吃五谷杂粮')

#定义函数
def fun(obj):
    obj.eat()
#开始调用函数
fun(Cat())
fun(Dog())
fun(Animal())

fun(Person())
#猫吃鱼
#狗吃骨头
#动物会吃

#人吃五谷杂粮  #person没有继承animal方法，但是person这个对象有eat方法，所以它也会调用eat方法
#把这个就叫做 鸭子类型 ， python是一门动态语言，可以在创建对象之后，动态的绑定属性和方法
#动态语言的多态崇尚“鸭子类型”，当看到一只鸟走起来像鸭子，游泳起来像鸭子，收起来也像鸭子，那么这只鸟就可以被称为鸭子。
#在鸭子类型中，不需要关心对象是什么类型，到底是不是鸭子，只关心对象的行为
#不需要关心person是谁的子类，只需要关心person是否具有eat的行为
'''
静态语言和动态语言关于多态的区别
静态语言实现多态的三个必要条件    #java是静态语言
a 继承
b 方法重写
c 父类引用指向子类对象
'''