'''
else语句
与else语句配合使用的三种情况
1. if...：
     ...
     else
     ...
                            1.  if条件表达式不成立时执行else
2. while...：
    ...
    else：
    ...

3. for...:
    ...
    else:
    ...
                 2 and 3： 没有碰到break时执行else

'''

#输入密码
'''
for item in range(3):
    passward=input('输入密码：')
    if passward=='8888':
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print('对不起，三次密码均输入错误')
   '''
a=0
while a<3:
    passward=input('输入密码')
    if passward=='8888':
        print('密码正确')
        break
    else:
        print('密码错误')
    a+=1   #改变变量，不可少
else:
    print('三次均错误')

'''while循环的执行流程
四步循环法
1.初始变化量
2.条件判断
3.条件执行体（循环体）
4.改变变量'''