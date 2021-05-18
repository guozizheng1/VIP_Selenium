from datetime import date, datetime
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius**2

    def __repr__(self):
        return '<圆形 半径是{}, 面积是{}>'.format(self.radius, self.area)


class Class:
    students = []

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<班级 {}>'.format(self.name)


class Publisher:
    def __init__(self, title, phone):
        self.title = title
        self.phone = phone


class Book:
    def __init__(self, title, author, price, publisher):
        self.title = title
        self.author = author
        self.price = price
        self.publisher = publisher

    def __repr__(self):
        return '<图书 {}>'.format(self.title)


class Student:
    students = []

    def __init__(self, name, gender, birthdate):
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        Student.students.append(self)

    @staticmethod
    def do_something():
        print('当前操作与类和实例无关！')

    @classmethod
    def get_students_num(cls):
        return len(cls.students)

    @property
    def age(self):
        return date.today().year - self.birthdate.year

    @age.setter
    def age(self, value):
        # print('年龄不能赋值，必须通过生日计算')
        raise ArithmeticError('年龄不能赋值！')

    def __repr__(self):
        return '<Student: {}>'.format(self.name)

    def learning(self):
        print('{}同学在学习'.format(self.name))

    def read(self, book):
        print('{} 在读《{}》书'.format(self.name, book.title))

if __name__ == '__main__':
    c1 = Class('A0001')

    s1 = Student('Tom', '男', date(1990, 3, 3))
    s2 = Student('Jerry', '女', date(1992, 4, 5))

    c1.students.append(s1)
    c1.students.append(s2)
    # Student.students.append(s2)

    # for s in Student.students:
    #     print(s)
    #
    # print('现在一共有{}个学生实例'.format(Student.get_students_num()))
    # Student.do_something()
    p = Publisher('清华大学出版社', '010 82931782')

    b1 = Book('Python精讲', 'Peter', 59.00, p)
    print(b1.publisher.phone)
    print(c1.students[0].age)
