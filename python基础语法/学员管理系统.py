"""
1.添加学员
2.删除学院
3.修改学员信息
4.查询学员信息
5.显示所有学员信息
6.退出系统
"""

# 定义学员信息
student_list = [{'id': 1, 'name': 'mike', 'age': 18},
                {'id': 2, 'name': 'ben', 'age': 20},
                {'id': 3, 'name': 'lily', 'age': 19}
                ]


# 显示界面函数
def view_info():
    print('-' * 20, end=' ')
    print('学员管理系统', end=' ')
    print('-' * 20)
    print('  1.添加学员\t\t2.删除学员\t\t\t3.修改学员信息\n  4.查询学员信息\t5.显示所有学员信息\t6.退出系统')


# 添加学员函数
def add_stu():
    new_id = int(input('请输入id:'))
    new_name = input('请输入姓名:')
    new_age = int(input('请输入年龄:'))
    for i in student_list:
        if new_id == i['id'] or new_name == i['name']:
            print('id或名字已存在')
            return
    dict1 = dict()
    dict1['id'] = new_id
    dict1['name'] = new_name
    dict1['age'] = new_age
    student_list.append(dict1)
    print('添加成功!')


# 删除学员函数
def del_stu():
    del_name = input('请输入名字:')
    for i in student_list:
        if del_name == i['name']:
            student_list.remove(i)
            print('删除成功!')
            return
    print('学员不存在')


# 修改学员信息
def mod_stu():
    mod_name = input('请输入学员名字:')
    for i in student_list:
        if mod_name == i['name']:
            new_age = int(input('请输入修改后数据:'))
            i['age'] = new_age
            print('修改成功!')
            return
    print('学员不存在')


# 查询学员信息
def que_stu():
    que_name = input('请输入查询学员名字:')
    for i in student_list:
        if que_name == i['name']:
            stu_id, name, age = i
            print(f'id={i.get(stu_id)}\tname={i.get(name)}\tage={i.get(age)}')
            return
    print('学员不存在')


# 查询学员所有信息
def que_all():
    for i in student_list:
        stu_id, name, age = i
        print(f'id={i.get(stu_id)}\tname={i.get(name)}\tage={i.get(age)}')
        print()


# 学员管理系统界面
while 1:
    view_info()
    num = int(input('请输入操作代码:'))
    if num == 1:
        add_stu()
    elif num == 2:
        del_stu()
    elif num == 3:
        mod_stu()
    elif num == 4:
        que_stu()
    elif num == 5:
        que_all()
    elif num == 6:
        break
    else:
        print('输入有误，请输入1~6之间的数字')
