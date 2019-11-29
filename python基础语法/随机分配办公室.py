import random
# 定义数据
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
offices = [[], [], []]

# 随机分配老师进入办公室
for name in teachers:
    num = random.randint(0, 2)
    offices[num].append(name)

# 遍历办公室中的人
i = 1
for office in offices:
    print(f'{i}号办公室的人数有{len(office)}人，老师分别是:')
    for name in office:
        print(name, end='\t')
    print()
    i += 1
