def func(a, b, c):
    print(a, b, c)


def func_2(a, b, *args):  # 带一个星号的当做元组来处理(可变长度参数)
    print(a, b, args)


def func_3(a, b, **kwargs):  # 带两个星号的当做字典表处理(关键字参数)
    print(a, b, kwargs)


def func_4(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)
    # print(a, b, args, kwargs)

if __name__ == '__main__':
    t = (99, 22, 88)
    dict = {'name': 'Tom', 'age': 30, 'salary': 5000}
    func_4(1, 2, *t, **dict)  # 函数解包
