'''
assert 断言
检查表达式
'''

def func(a,b):
    assert (b > 0),'除数不能为0'
    result = a / b
    print(result)

if __name__ == '__main__':
    func(8,0)