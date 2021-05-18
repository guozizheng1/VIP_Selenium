def say_hello():
    print('Hello')


def func():
    return 10


def greeting(name):
    print('你好{}'.format(name))


def add(a,b):
    #print(a+b)
    return a + b


def times(a,b):
    return a * b


def add_num(n):
    n += 10
    return n


def change_list(l):
    l[0] = 99

lst = [1,2,3]
print(lst)
change_list(lst.copy())
print(lst)


# x = 5
# print('x={}'.format(x))
# print(add_num(x))
# print('x={}'.format(x))

