'''
函数的参数传递

一.函数调用的参数传递
1.位置实参
根据形参对应的位置进行实参传递

2.关键字实参
根据形参名称进行实参传递
calc(b=10,a=30)
   #b形参名称， 10是实参数
   #b传参给下面的b
   #a,b称为形式参数，简称形参，形参的位置是在函数的定义处
def calc(a,b)

二.函数调用的参数传递内存分析图


'''

#一.
def calc(a,b):   #a,b称为形式参数，简称形参，形参的位置是在函数的定义处
    c=a+b
    return c
result=calc(10,30)  #10，30称为实际参数的值，简称实参，实参的位置是函数的调用处
print(result)

#二.
def fun(arg1,arg2):
    print('arg1',arg1)
    print('arg2',arg2)
    arg1=100
    arg2.append(10)
    print('arg1', arg1)
    print('arg2', arg2)   #函数的创建
    #return 此处没有返回值，所以可以省略

n1=11
n2=[22,33,44]
print('n1',n1)
print('n2',n2)
fun(n1,n2)  #位置传参，
#arg1，arg2 是函数定义处的形参，n1,n2 是函数调用处的实参，可以得出，实参名称与形参名称可以不一致
print('n1',n1)
print('n2',n2)

# n1 11
# n2 [22, 33, 44]
# arg1 11
# arg2 [22, 33, 44]
# arg1 100
# arg2 [22, 33, 44, 10]
# n1 11
# n2 [22, 33, 44, 10]

#在函数调用过程中，进行参数的传递
#如果是不可变对象，在函数体内的修改不会影响实际实参的值（n1是int 不可变类型，在fun这个函数体内虽然修改为100，函数体执行完毕仍然是11
# arg1的修改，不会影响n1的值）   整数，字符串，元组
#如果是可变对象，在函数体内的修改会影响到实参的值（arg2的修改，append（10），会影响n2的值）   列表，字典