def hello():
    print('hello')


def cal(a, b):
    return a / b

if __name__ == '__main__':
    try:
        print(cal(5, 0))
    except ValueError:
        print('值有错误')
    except ZeroDivisionError:
        print('不能除0')
    except Exception as ex:
        print('计算出现了错误')

