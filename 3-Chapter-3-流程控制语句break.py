'''
流程控制语句break
用于结束循环结构，通常与分支结构if一起使用
非正常结束循环，比如ATM取款，输入3次后，直接退卡，如果正确就结束循环
'''
for item in range(3):
    passward=input('输入密码')
    if passward=='8888':
        print('passward is right')
        break
    else:
        print('passward is wrong')

#输入密码7777
passward is wrong
输入密码9999
passward is wrong
输入密码4567
passward is wrong

#改成while循环
a=0  #初始化变量
while a<3:
    passward==input('输入密码：')       #line24-29  循环体
    if passward=='8888':
        print('passward is right')
        break
    else:
        print('passward is wrong')
    a+=1     #改变变量

'''while循环的执行流程
四步循环法
1.初始变化量
2.条件判断
3.条件执行体（循环体）
4.改变变量'''