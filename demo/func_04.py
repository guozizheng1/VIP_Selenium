x = 99  # 全局变量 global


def func_a():
    global x  # 将x声明为全局的x变量
    x = 10  # 本地变量 local
    print(x)


def func_b():
    y = 10  # 封装

    def sub_func():
        nonlocal y   # 将y声明为非本地变量可以影响外侧的变量
        y = 100
        print(y)
    print(y)
    sub_func()
    print(y)

if __name__ == '__main__':
    func_a()
