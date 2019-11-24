# 定义变量
name = "mike"
age = 18
height = 175.5
studentId = 1

# 输出字符串用%s
print("我的名字叫%s" % name)

# 输出整数用%d,限定位数使用%xyd，y为限定位数，x为用x补全位数
print("我的年龄是%d" % age)
print("我的学号是%03d" % studentId)

# 输出小数用%f，限定小数位数用%.xf，x为保留x位小数
print("我的身高为%.2f" % height)

# 同时输出多个数据使用元组
print("我的名字叫%s,今年%d岁,身高是%.2dcm" % (name, age, height))

