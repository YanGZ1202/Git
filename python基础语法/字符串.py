"""
切片
"""
# 序列名[开始位置:结束位置(不包含):步长]
str1 = 'abcdefgh'
print(str1[2:6])
print(str1[1:8:2])
print(str1[:6])
print(str1[1:])
print(str1[:])

# 负数值
print(str1[::-1])  # 倒序
print(str1[-4:-1])
print(str1[-4:-1:1])
print(str1[-4:-1:-1])  # 不能获取数据，选取方向和步长方向冲突
print(str1[-1:-4:-1])


"""
查找
"""
str2 = 'hello world and python and java'
# find(子串，开始，结束)返回出现的下标，否则返回-1；用index()当字符串不存在报错
print(str2.find('and'))  # 12
print(str2.find('and', 15, 30))  # 23
print(str2.find('php'))  # -1
# print(str2.index('php'))
# count(子串，开始，结束)统计出现次数
print(str2.count('and'))  # 2


"""
替换
"""
# replace('旧子串','新子串',替换次数)不改变原有字符串，说明字符串是不可变类型
print(str2.replace('and', 'hhh'))
print(str2.replace('and', 'hhh', 1))
# split分割字符串，返回一个列表，且丢失分隔符
myList = str2.split('and', 1)
print(myList)
# join()合并列表中的字符串数据为一个大字符串
myList1 = ['i', 'he', 'you', 'she']
newStr = 'and'.join(myList1)
print(newStr)

