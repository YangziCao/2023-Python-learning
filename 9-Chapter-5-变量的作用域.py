'''
变量的作用域
  程序代码能访问该变量的区域

根据变量的有效范围分为
1.局部变量
在函数内定义并使用的变量，只在函数内部有效，局部变量使用global声明，这个变量就会称为全局变量

2.全局变量
函数体外定义的变量，可作用于函数内外
'''

def fun(a,b):
    c=a+b      #c,称为局部变量，因为c是在函数体内进行定义的变量，a，b为函数的形参，作用范围也是函数内部，相当于局部变量
    print(c)

#print(a)
#print(c)
#line17 and 18 函数体外输出会报错，因为a,c超出了起作用的范围，超出了作用域

name='杨老师'  #name的作用范围为函数内部和外部都可以使用，称为全局变量
print(name)
def fun2():
    print(name)
#调用函数
fun2()

def fun3():
    age=20
    print(age)
fun3()
#如果想在函数的外面输出age的值，如下加入global

def fun4():
    global age  #函数内部定义的变量，局部变量，局部变量使用global声明，这个变量实际上就是全局变量
    age=30
    print(age)
fun4()
print(age)