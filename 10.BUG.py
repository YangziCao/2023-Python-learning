'''
一.bug由来
飞蛾钻进计算机中，引起计算机故障，计算机之母称其为bug

debug

二. bug的常见类型
1.粗心导致得语法错误 syntaxError
宝典
a. 漏了末尾得冒号，如if语句，循环语句，else语句等
b. 缩进错误，该缩进得没缩进，不该缩进得瞎缩进
c. 把英文字符错写为中文字符，如引号，冒号，括号
d. 字符串拼接得时候，把字符串和数字拼在一起
e. 没有定义变量，比说说while的循环条件的变量
f. “==”比较运算符 和“=”赋值运算符的混用



2.知识点不熟练导致的错误
a. 索引越界问题 IndexError

lst=[11,22,33,44]
print(1st[4])
计算机中的序列从0开始的，4不存在

b. append()方法的使用掌握不熟练

lst=[]
lst=append('A','B','C')
print(lst)

append的添加方法是 lst.append（）  不是=
而且append的方法只能每次添加一个元素



3. 思路不清导致的问题解决方案
a.使用print（）函数，进行验证，查找问题
b.使用“#”暂时注释部分代码



4. 被动掉坑：程序代码逻辑没有错，只是因为用户错误操作或者一些‘例外情况’而导致的程序崩溃

解决方案：
Python提供了异常处理机制，可以在异常出现时及时捕获，然后内部‘消化’，让程序继续运行
try：
except：

python的异常处理机制
a. try...except...结构
b. 多个except结构
捕获异常的顺序按照先子类后父亲类的顺序，为了避免遗漏可能出现的异常，可以在最后增加BaseException
c. try...except...else结构
如果try块中没有抛出异常，则执行else块，如果try中抛出异常，则执行except块
d. try...except...else...finally结构
finally块无论是否发生异常都会被执行，能常用来释放try块中申请的资源

'''
#4.
#a.
try:
    a=int(input('输入第一个整数'))
    b=int(input('输入第二个整数'))
    result=a/b
    print('结果为：',result)
except ZeroDivisionError:
    print('sorry,除数不能为0')
print('程序结束')
#输入第一个整数10
#输入第二个整数0
#sorry,除数不能为0
#程序结束


#b.
try:
    a=int(input('输入第一个整数'))
    b=int(input('输入第二个整数'))
    result=a/b
    print('结果为：',result)
except ZeroDivisionError:
    print('sorry,除数不能为0')
except ValueError:
    print('只能输入数字串')   #除法计算中出现的2个异常都可以捕获了   除数不能为0和只输出数字串
except BaseException as e:
    print(e)
print('程序结束')


#c.
try:
    a=int(input('输入第一个整数'))
    b=int(input('输入第二个整数'))
    result=a/b
except BaseException as e:
    print('出错了',e)
else:
    print('结果为：', result)


#d.
try:
    a=int(input('输入第一个整数'))
    b=int(input('输入第二个整数'))
    result=a/b
except BaseException as e:
    print('出错了',e)
else:
    print('结果为：', result)
finally:
    print('谢谢使用')

'''
三. Python中常见的异常类型
1. ZeroDivisionError  除（或取模）零（所有数据类型）
2. IndexError         序列中没有此索引（Index）
3. KeyError           映射中没有这个键
4. NameError          未声明/初始化对象（没有属性）
5. SyntaxError        Python语法错误
6. ValueError         传入无效的参数
'''

#5
#int a=20 SyntaxError
#Python中变量a没有数据类型，而 int a 相当于给变量设置类型，语法错误

'''
四.python的异常处理机制--traceback模块
使用traceback模块打印异常信息
'''
#print(10/0)
import traceback
try:
    print('----------------------------')
    print(1/0)
except:
    traceback.print_exc()
#Traceback (most recent call last):
#  File "D:\PyCharm-Project\venv\10.BUG.py", line 136, in <module>
#    print(1/0)
#          ~^~
#ZeroDivisionError: division by zero

#作用，这些异常的信息有可能在后续中被存入到文件当中，放到日志文件