'''
一. 字符串的查询操作方法
1. index（） 查找子串substr第一次出现的位置，如果查找的子串不存在，则抛出ValueError
2. rindex() 查找子串substr最后一次出现的位置，如果查找的子串不存在，则抛出ValueError
3. find（）  查找子串substr第一次出现的位置，如果查找的子串不存在，则返回-1
4. rfind（） 查找子串substr最后一次出现的位置，如果查找的子串不存在，则抛出-1

r是 rear的意思，指后面，背面
'''
s='hello,hello'   # 正向索引0-10（，也算一个），逆向索引-1到-11
print(s.index('lo'))  #3
print(s.find('lo'))   #3
print(s.rindex('lo'))  #9
print(s.rfind('lo'))  #9

'''
二. 字符串的大小写转换操作
1. upper()  把字符串中的所有字符都转成大写字母
2. lower（） 把字符串中的所有字符都转成小写字母
3. swapcase() 把字符串中所有大写字母转成小写字母，把所有小写字母转为大写字母
4. capitalize（） 把第一个字符转换成大写，把其余字符转换为小写
5. title（） 把单个单词的第一个字符转换成大写，把每个单词的剩余字符转换为小写
'''

# 1.
s='hello,python'
a=s.upper()   #转成大写之后，会产生一个新的字符串对象
print(a) #HELLO,PYTHON
print(s) #hello,python

# 2.
b=s.lower()
print(b)
print(b==s)  # True   b和s内容相等
print(b is s) # False  但是地址不同


#3.
s2='hello,Python'
print(s2.swapcase())
# HELLO,pYTHON

#4.
print(s2.capitalize())
# Hello,python

#5.
print(s2.title())
#Hello,Python


'''
三. 字符串内容对齐操作的方法
1. center() 居中对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串
2. ljust() 左对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串
3. rjust() 右对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串
4. zfill() 右对齐，左边用0填充，该方法只接受一个参数，用于指定字符串的宽度，如果指定的宽度小于等于字符串的长度，返回字符串本身
'''

#1.居中对齐
s='hello,Python'   #12个字符
print(s.center(20,'*'))
#****hello,Python****
#指定宽度为20，12个字符，还有8个空，左右各4个

#2.左对齐
print(s.ljust(20,'*'))
# hello,Python********
print(s.ljust(10,'*'))
# hello,Python
# 如果设置的宽度小于字符串本身，就返回原字符串

#如果不写填充符，可以默认是空格
print(s.ljust(20))
#hello,Python        (后面有8个空格)

#3.右对齐
print(s.rjust(20,'*'))
# ********hello,Python

#4. 右对齐
print(s.zfill(20))  #左边用0填充，该方法只接受一个参数，用于指定字符串的宽度
#00000000hello,Python

print('-8910'.zfill(8))    #-8910  共5个字符
#-0008910
#0添加到了符号的后面


'''
四. 字符串劈分操作
1. split() 
从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
以通过参数sep指定劈分字符串的劈分符
通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独作为一部分

2.rsplit()
从字符串的右边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
以通过参数sep指定劈分字符串式的劈分符
通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独作为一部分
'''

#1.
s='hello world python'
lst=s.split()
print(lst)
# ['hello', 'world', 'python']   默认从空格开始劈分

s1='hello|world|Python'
print(s1.split(sep='|'))
#['hello', 'world', 'Python']

print(s1.split(sep='|',maxsplit=1))
#['hello', 'world|Python']   #以|劈分，只劈分一次

#2. rsplit
print(s.rsplit())
# ['hello', 'world', 'python']
print(s1.rsplit(sep='|'))
# ['hello', 'world', 'Python']
print(s1.rsplit(sep='|',maxsplit=1))
#['hello|world', 'Python']

'''
五. 判断字符串操作的方法
1. isidentifier() 判断指定的字符串是不是合法的标识符
2. isspace()      判断指定的字符串是否全部由空白字符组成（回车，换行，水平制表符）
3. isalpha()      判断指定的字符串是否全部由字母组成
4. isdecimal()   判断指定的字符串是否全部由十进制的数字组成
5. isnumeric()    判断指定的字符串是否全部由数字组成
6. isalnum()      判断指定的字符串是否全部由字母和数字组成
'''