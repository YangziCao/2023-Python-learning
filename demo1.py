#
print (520)
print('hello world')
print(3+1)

#print()函数可以将内容输出的目的地
# 1.显示器/控制台  2.文件
#print()函数的输出形式
# 1.换行  2.不换行

#将数据输出到文件中
#注意点1.所指定的盘符存在   2. 使用file=xx的形式
fp=open('D:/PyCharm-Project/text.txt','a+') #如果文件不存在就创建，如果存在就在文件内容后面继续添加
#a+表示如果有这个文件，它不会覆盖掉，只会添加在原始文件的后面
print('hello world',file=fp)
fp.close()
#如果第14line 不加file= 那么print 的text里面就是空白的
#.如果不想换行输出的话（输出内容在一行中）
print('hello','world2','python')
#使用逗号进行分隔的话，会在一行输出



#转义字符
print('hello\nworld')#换行输出
print('hello\tworld')#4个字母是一个制表位，he11是一个，0后面还要3个空格
print('helloooo\tworld')#o后面四个空格，helloooo  8个字母占满了
#占满就重新开一个，不满就补全
print('hello\rworld')
#输出出来只有world，return返回首位，world覆盖掉hello了。

print('hello\bworld')
#输出出来hello的o消失，\b是退一个格

print('http:\\www.baidu.com')
#这样输出的话结果是这样http:\www.baidu.com，少一个\,第二个\相当于转义功能，但又不是转义的首字母
print('http:\\\\www.baidu.com')
#这样就ok

print('The teacher said:"hello"')
#print('The teacher said:'hello'')#这样会报错，输出的结果中包含单引号，写一个\就可以，那么单引号不再是字符串的边界，而是字符串中应该输出的内容
print('The teacher:\'hello\'')

#原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r或者R
#print('hello\nworld') 本来是换行输出
print(r'hello\nworld')
#输出结果 hello\nworld
#Notice 原始字符串的最后一个字母不能是反斜线
#print(r'hello\nworld\')
      #如上，就会报错，但是2个\就可以
print(r'hello\nworld\\')

#二进制与字符编码
#Unicode   #UTF-8
print(chr(0b100111001011000))
print(ord('乘'))
#output
#乘
#20056  是乘的十进制

#Python中的标识符和保留字
#有有一些单词被赋予了特定的意义，这些单词你再给你的任何对象起名字的时候都不能用
# import keyword print(keyword.kwlist)
#变量，函数，类，模块和其他对象的起的名字就叫标识符
#规则
#1.字母，数字，下划线
#2.不能以数字开头
#3.不能是保留字
#4.严格区分大小写

#变量的定义和使用
#变量是内存中一个带标签的盒子
name='maliya'
print(name)
#output   maliya

#变量由三部分组成
#1.标识：表示对象所存储的内存地址，使用内置函数id（obj）来获取
#2.类型：表示的是对象的数据类型，使用内置函数type（obj）来获取
#3.值：表示对象所存储的具体数据，使用print（obj）可以将值进行打印输出

#eg
print('标识',id(name))
print('类型',type(name))
print('值',name)

#当多次赋值之后，变量名会指向新的空间
name='maliya'
name='chuliubing'
print(name)
#output chuliubing

#常用的数据类型
#1.整数类型 → int → 98
#2.浮点数类型 → float → 3.14159
#3.布尔类型 → bool → True, False
#字符串类型 → str → ’人生苦短，我用python‘  #只要加上单引号/双引号/三引号，则为字符串类型

#1.整数类型
#英文为integer,简写为int，可以表示正数，负数和零
#整数的不同进制表示方式
#十进制→默认的进制
#二进制→以0b开头
#八进制→以0o开头
#十六进制→以0x开头
n1=90
n2=-76
n3=0
print(n1)
print(n2)
print(n3)
#查看变量类型
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))
#整数可以表示为十进制，二进制，八进制，十六进制
print('十进制',118)
print('二进制',0b10101111) #注意要加0b，不然会默认为十进制
print('八进制',0o176) #0o开头
print('十六进制',0x1eaf)  #十六进制的16个数是 0123456789ABCDEF,不区分大小写

#2.浮点类型
#浮点数由整数部分和小数部分组成
#浮点数存储不精确性（使用浮点数进行计算时，可能会出现小数位数不确定的情况）
print(1.1+2.2)  #output 3.3000000000000003
#原因是计算机采用二进制存储，所以存储浮点数的时候是不精确的，会存在误差
#解决方案
#导入模块decimal
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2')) #Decimal 中的D要大写
#output 3.3
#也不是所有的浮点数相加都有误差，如下就无。
print(1.1+2.1)  #output 3.2

a=3.14159
print(a,type(a))  #output 3.14159 <class 'float'>

#3.布尔类型  bool 原型为 boolean
#用来表示真或假的值
#True为真，False为假  二者首字母需大写！！!
#布尔值可以转化为整数
#True→1
#Flase→0
f1=True
f2=False
print(f1,type(f1))  #output: True <class 'bool'>
print(f2,type(f2))  #output: False <class 'bool'>

#布尔值可以转化为整数计算
print(True+1)   #output 2  1+1的结果为2，True表示1
print(False+1)  #output 1  0+1的结果为1，False表示0

#4.字符串类型
#又被称为不可变的字符序列
#可以使用单引号，双引号，三引号来定义
#单引号和双引号定义的字符串必须在一行
#三引号定义的字符串可以分布在连续的多行

str1='Python'
str2="Python"  #如果不在一行打的话，它会再每行自己加上引号,如果删除多余的话，就会报错。
str3="""Python，
Java"""
str4='''Python, 
Java'''
print(str1,type(str1)) #output: Python <class 'str'>
print(str2,type(str2)) #output: Python <class 'str'>
print(str3,type(str3))
#output: Python,
#Java <class 'str'>
print(str4,type(str4))

#数据类型转换
#为什么需要数据类型转换
#因为需要将不同数据类型拼接在一起

name='zhangsan'
age=20
print(type(name),type(age))
#output: <class 'str'> <class 'int'>
#说明name 和 age的数据类型不同，一个为字符串，一个为整数
#  如果输入这个，print('我叫'+name+'今年'+age+'岁')
#TypeError: can only concatenate（连接） str (not "int") to str
#当将str类型与int类型进行连接时，报错，解决方案就是类型转换

print('我叫'+name+'今年'+str(age)+'岁')
#output: 我叫zhangsan今年20岁
#将int类型通过str（）函数转成了str函数

#  str()将其他类型转成str类型
a=10
b=198.8
c=False
print(type(a),type(b),type(c))  #output: <class 'int'> <class 'float'> <class 'bool'>布尔类型
print(str(a),str(b),str(c))     #output: 10 198.8 False
print(type(str(a)),type(str(b)),type(str(c)))
#output: <class 'str'> <class 'str'> <class 'str'> 说明转化成功

#  int()将其他类型转换成int类型
s1='128'
s2='76.77'
s3='hello'
f1=98.7  # 带引号就是字符串，
ff=True
print(type(s1),type(s2),type(s3),type(f1),type(ff))  #output: <class 'str'> <class 'str'> <class 'str'>  <class 'float'> <class 'bool'>
print(int(s1),type(int(s1)))  #output:  128 <class 'int'>     将str转成int类型，字符串为数字串
#print(int(s2),type(int(s2))) #output： 报错，将str转成int类型，  因为字符串为小数串
#print(int(s3),type(int(s3)))  #output:  报错，将str转成int类型时，字符串必须为数字串，且为整数。非数字串不可转换。
print(int(f1),type(int(f1)))  #output： 98 <class 'int'>      将float转成int类型，截取整数部分，舍掉小数部分
print(int(ff),type(int(ff)))  #output:  1 <class 'int'>

# float()函数，将其他类型数据转为float类型
s1='128.98'
s2='76'
s3='hello'
ff=True
i=98
print(type(s1),type(s2),type(s3),type(ff),type(i)) #output: <class 'str'> <class 'str'> <class 'str'> <class 'bool'> <class 'int'>
print(float(s1),type(float(s1)))   #output: 128.98 <class 'float'>
print(float(s2),type(float(s2)))   #output: 76.0 <class 'float'>
#print(float(s3),type(float(s3)))  #output  Error   字符串中的数据如果是非数字串，则不允许转换
print(float(ff),type(float(ff)))   #output  1.0 <class 'float'>
print(float(i),type(float(i)))     #output  98.0 <class 'float'>

#Python中的注释
#注释：在代码中对代码的功能进行解释说明的标注性文字，可以提高代码的可读性
#注释的内容会被Python解释器忽略
#通常包括三种类型的注释
#1.单行注释：以#开头，直到换行结束
#2.多行注释：没有单独的多行注释标记，将一对三引号之间的代码称为多行注释
#3.中文编码声明注释：在文件开头加上中文声明注释，用指定源码文件的编码格式

#输入函数input
#present=input('大圣想要什么礼物呢？')
#print(present,type(present))

#a=input('请输入一个加数')
#b=input('请输入另一个加数')
#print(a+b)
#说明并没有进行a+b的整数运算，而是起了一个连接作用
#print(type(a),type(b))   #output: <class 'str'> <class 'str'>
#所以加号只起到连接作用
#解决办法：将a，b的str类型转换为int类型
#a=input('请输入一个加数')
#a=int(a)
#b=input('请输入另一个加数')
#b=int(b)
#print(a+b)              #output: 30
#print(type(a),type(b))  #output: <class 'int'> <class 'int'>
#如此写太过麻烦

#a=int(input('请输入一个加数'))
#b=int(input('请输入另一个加数'))
#print(a+b)              #output: 30
#print(type(a),type(b))  #output: <class 'int'> <class 'int

#运算符
#A. 算术运算符
print(1+1)
print(1-1)
print(2*4)
print(1/2)
print(11/2)
print(11//2)  #整除运算     output: 5
print(11%2)   #取余运算     output：1
print(2**3)   #表示2的3次方 output: 8

#一正一负的运算
print(9//4)   # 2
print(-9//-4) # 2
print(9//-4)  #-3  一正一负向下取整（整除运算）
print(-9//4)  #-3  一正一负向下取整（整除运算）
print(9%-4)   #-3  取余一正一负要遵循公式    →  余数=被除数-除数*商   余数=9-（-4）*（-3）=-3  （商本来是 -2，但是一正一负的整除运算向下取整）
print(-9%4)   #3     余数=被除数-除数*商   余数=-9-4*（-3）

#B. 赋值运算符
#运算顺序从右到左
i=3+4
print(i)

#支持链式赋值  → a=b=c=20 将20赋给c，将20赋给b，将20赋给a
a=b=c=20
print(a,id(a))   #.标识：表示对象所存储的内存地址，使用内置函数id（obj）来获取   Line78
print(b,id(b))
print(c,id(c))
#output: 20 140723434612104
#output: 20 140723434612104
#output: 20 140723434612104
#链式赋值只有一个整数对象，但是却有abc三个引用在指向这个位置

#支持参数赋值
a=20
a+=30
print(a)         #50  相当于a加上30，再赋值给a

a-=10
print(a)         #40  相当于a-10再赋值给a

a*=2
print(a)         #80
print(type(a))   # <class 'int'>

a/=3
print(a)         # 26.666666666666668
print(type(a))   # <class 'float'>

a//=2            # //整除
print(a)         # 13.0
print(type(a))   #<class 'float'>

a%=3
print(a)         # 1.0

#支持系列解包赋值→ a,b,c=20,30,40   指将40赋值给c，30赋值给b，20赋给a，要求等号两侧的变量个数和值的个数要相同
#解包赋值
a,b,c=20,30,40
print(a,b,c)     #20,30,40
#解包赋值的优点：其他语言如果要实现2个变量的交换，可能需要中间变量，但是python不需要
#eg 交换2个变量的值
a,b=10,20
print('交换之前:',a,b)
#交换
a,b=b,a
print('交换之后:',a,b)
#output:  交换之前: 10 20   交换之后: 20 10

#C. 比较运算符
#对变量或表达式的结果进行大小，真假等比较
#比较运算符的结果为bool类型
#  >,<,>=,<=,!=（不等于）
#  ==  →对象value的比较
#  is, is not,  →  对象的id的比较

a,b=10,20
print('a>b吗？',a>b)  #output: False
print(a>b)           #output: False
print(a<b)           #output: True
print(a<=b)          #output: True
print(a>=b)          #output: Flase
print(a==b)          #output: Flase   (一个=是赋值运算符，2个==是比较运算符)
print(a!=b)          #output: True
#一个变量由三部分组成，标识，类别，值
# ==比较的是值还是标识（id）呢？
# 比较的是值
# 比较对象的标识，使用的是is
a=10
b=10
print(a==b)     #output: True  说明a与b的value相等
print(a is b)   #output: True  说明a与b的id标识相等

lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)     #value   True
print(lst1 is lst2)   #id      False
print(id(lst1))       # 1872802963456
print(id(lst2))       # 1872803211136

print(a is not b)       # False  a的id和b的id是不相等的  LINE348
print(lst1 is not lst2) # True

#D. 布尔运算符
#and, or, not, in, not in
a,b=1,2  #解包运算符
print(a==1 and b==2) #True   true and true → true
print(a==1 and b<2)  #Flase  ture and flase → flase
print(a!=1 and b==2) #Flase  flase and true →  flase
print(a!=1 and b!=2) #Flase  flase and flase →  flase

print(a==1 or b==2) #True  ture or ture → true
print(a==1 or b<2)  #True  ture or flase → true
print(a!=1 or b==2) #True  flase or true →  true
print(a!=1 or b!=2) #Flase  flase or flase →  flase

f=True
f2=False
print(not f)  #flase
print(not f2) #true

s='helloworld'
print('w' in s)     # t
print('k' in s)     # f
print('w' not in s) # f
print('k' not in s) # t

#E. 位运算符
#将数据转为二进制进行计算
# 位与& → 对应数位都是1，结果数位才是1， 否则为0
# 位或| → 对应数位都是0，结果数位才是0，否则为1
# 左移位运算符 👉 高位溢出舍弃，低位补0
# 右移位运算符 👉 低位溢出舍弃，高位补0

print(4&8)  # 0
#按位与&，同为1时，结果位1

print(4|8) # 12
#按位或|

#左移乘2，右移除2
print(4<<1) #左移1位   8
print(4<<2) #左移2位   16

print(4>>1)  #2
print(4>>2)  #1

#运算符的优先级
# 先算算术运算符， 先幂乘除后加减
# 再算位运算，  移位，按位与，按位或
# 然后是比较运算符
# 再是布尔运算符
# 最后是赋值运算符
# 有括号先算括号，括号优先级最高