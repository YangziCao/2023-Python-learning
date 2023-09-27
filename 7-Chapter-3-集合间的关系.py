'''
集合间的关系
1.两个集合是否相等
可以使用运算符==或！=进行判断

2.一个集合是否是另一个集合的子集
 可以调用方法issubset进行判断
 B是A的子集

3. 一个集合是否是另一个集合的超集
可以调用方法issuperset进行判断

4. 两个集合是否没有交集
可以调用方法 isdisjoint进行判断
'''
#1.
s={10,20,30,40}
s2={30,40,20,10}
print(s==s2)  #True
print(s!=s2)  #False
#集合是无序的，只要它们的内容相同，底层的存储顺序就是相同的


#2.一个是否是另一个的子集
s1={10,20,30,40,50,60}
s2={10,20,30,40}
s3={10,20,90}
print(s2.issubset(s1)) # True
print(s3.issubset(s1)) # False

#3. 一个集合是否是另一个的超集
print(s1.issuperset(s2)) # True
print(s1.issuperset(s3)) # False

#4.两个集合是否没有交集  是否没有！
print(s2.isdisjoint(s3)) # False

s4={100,200,300}
print(s2.isdisjoint(s4)) # True



