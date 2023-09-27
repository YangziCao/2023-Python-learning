'''
用于生成集合的公式
{i*i for i in range(1,10)}
将列表生成式的[]改为 {}就ok
'''

#列表生成式
lst=[i*i for i in range(6)]
print(lst)
#[0, 1, 4, 9, 16, 25]

#集合生成式
s={i*i for i in range(6)}
print(s)
# {0, 1, 4, 9, 16, 25}

s={i*i for i in range(10)}
print(s)
#{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}