# def func(a, b, c=5):
#     print('a={}, b={}, c={}'.format(a,b,c))
#
#
# # def avg(a, b):
# #     return (a + b)/2
# #
# #
# # def avg_3(a,b,c):
# #     return (a + b + c)/3


def func(a, *args):
    print(a, args)


def func_avg(a, *args):
    num = len(args) + 1
    return (a + sum(args))/num

if __name__ == '__main__':
    t = (99, 80, 100)
    print(func_avg(79, *t))  # 解包
