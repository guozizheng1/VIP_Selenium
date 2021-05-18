class Super:
    def method(self):
        print('这是基类的方法')


class Inheritance(Super):
    pass


class Replacer(Super):
    def method(self):
        print('这是派生类的方法')

class Extender(Super):
    def method(self):
        Super.method(self)
        print('这是派生类在执行基类行为基础之上的额外操作')

if __name__ == '__main__':
    i = Inheritance()
    R = Replacer()
    e = Extender()
    e.method()
    R.method()