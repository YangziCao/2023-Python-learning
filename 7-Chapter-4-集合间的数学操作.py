'''
集合的数学操作

交集，并集，差集，对称差集
'''

#1.交集
s1={10,20,30,40}
s2={20,30,40,50,60}
print(s1.intersection(s2))
# {40, 20, 30}
#或者使用符号&求交集
print(s1&s2)
print(s1 & s2)  #中间有无空格都可，有空格美观点


#2.并集
print(s1.union(s2))
# {40, 10, 50, 20, 60, 30}
#或者使用符号|
print(s1 | s2)
# {40, 10, 50, 20, 60, 30}


#3.差集
print(s1.difference(s2))
# {10}
# 或者使用符号 -  减号
print(s1-s2)
#{10}

#4.对称差集(集合的并集减去交集)
print(s1.symmetric_difference(s2))
# {50, 10, 60}
print(s1^s2)
#{50, 10, 60}

