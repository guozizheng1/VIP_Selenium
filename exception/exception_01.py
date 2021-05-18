try:
    n = int(input("请输入一个数字："))
    m = int(input("请再输入一个数字："))
    result = n / m
except TypeError:
    print('值类型有问题')

except ValueError as err:
    print('值有问题', err)

except ZeroDivisionError as zec:
    print('不能除零')
    # raise zec

except Exception as ec:
    print('其他错误', ec)

else:
    print(result)

finally:
    pass
