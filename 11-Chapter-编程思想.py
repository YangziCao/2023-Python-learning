'''
一.编程思想
编程届的两大阵营

                            面向过程                                    面向对象
区别             事物比较简单，可以用线性思维去解决             事物比较复杂，使用简单的线性思维无法解决
共同点      面向过程和面向对象都是解决实际问题得一种思维方式
           二者相辅相成，并不是对立的
           解决复杂问题，通过面向对象方式便于我们从宏观上把握事物之间复杂得关系，方便我们分析整个系统；具体到微观操作，仍然使用面向过程方式来处理


二.类与对象
1. 类：类别，分门别类，物以类聚，类是多个类似事物组成的群体的统称，能够帮助我们快速理解和判断事物的性质

2. 数据类型：
  不同的数据类型属于不同的类
  使用内置函数查看数据类型
  print(type(100))  <clasee 'int'>

3. 对象
100,99,520都是int类之下包含的相似的不同个例，这个个例专业术语称为  实例或对象
python中一切皆对象


三.类的创建
1.创建类的语法
class Student:
      pass
2.类的组成
a.类属性
b.实例方法
c.静态方法
d.类方法

'''

#三.
#1.创建类的语法
class Student:
    pass
#student 是类名，由一个或多个单词组成，每个单词对的首字母大写，其余小写。
#python当中一切皆对象，那么student是对象嘛？有空间吗？
print(id(Student))   #2072184063152
print(type(Student)) #<class 'type'>
print(Student)       #<class '__main__.Student'>

#2.类的组成
class Student:
    native_place='吉林'  #直接写在类里的变量，称为类属性
    def __init__(self,name,age):     #初始化方法
        self.name=name  #self.name 称为实例属性，进行了赋值的操作，将局部变量name的值赋给实例属性   实例也叫做对象。
        self.age=age



    #实例方法
    def eat(self):
        print('学生在吃饭')

    #静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以是静态方法')

    #类方法
    @classmethod
    def cm(cls):
        print('这是类方法，因为使用了classmethod进行修饰')

#在类之外定义的称为函数，在类之内定义的称为方法
def drink():
    print('喝水')


'''
四.对象的创建
对象的创建又称为类的实例化
语法：
    实例名=类名（）
意义：有了实例，就可以调用类中的内容

'''
#创建student类的对象
stu1=Student('张三',20)
print(id(stu1),type(stu1),stu1)
#2480651328464 <class '__main__.Student'> <__main__.Student object at 0x0000024192575BD0>

stu1.eat()         #对象名.方法名（）
#学生在吃饭
Student.eat(stu1)  #类名.方法名（类的对象）👉实际就是方法定义处的self
#学生在吃饭
#line87 and 89代码功能相同，都是调用student中的eat方法
print(stu1.name)
#张三


'''
五.类属性，类方法，静态方法
类属性：类中方法外的变量称为类属性，被该类的所有对象所共享
类方法：使用@classmethod修饰的方法，使用类名直接访问的方法
静态方法:使用@staticmethod修饰的方法，使用类名直接访问的方法
'''
print(Student.native_place)  #访问类属性
#吉林
Student.native_place='天津'
print(Student.native_place)
#天津
Student.cm()  #调用类方法
Student.sm()  #调用静态方法


'''
六.动态绑定属性和方法
python是动态语言，在创建对象之后，可以动态地绑定属性和方法
'''