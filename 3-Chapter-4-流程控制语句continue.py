'''
continue语句
用于结束当前循环，进入下一次循环，通常与分支结构中的if一起使用
'''

#题目要求：输出1-50之间所有5的倍数， 5，10，15...
#共同点，和5的余数为0的数，都是5的倍数

for item in range(1,51):
    if item%5==0:
     print(item)

#使用continue语句
for item in range(1,51):
    if item%5!=0:
        continue
    print(item)