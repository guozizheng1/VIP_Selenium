from datetime import date, datetime

class Person:
    def __init__(self, name, age, birthday, gender):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.gender = gender
        self._salary = 0.0  # 私有的

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value <= 0.00:
            self._salary = 0.00
        else:
            self._salary = value

    def say(self, word):
        print('{}说: {}'.format(self.name, word))

    def __str__(self):
        return '<Person: {}>'.format(self.name)

    def get_age(self):
        return date.today().year - self.birthday.year


if __name__ == '__main__':
    p1 = Person('张三', 20, date(1996, 3, 1), '男')
    p1.salary = -5000
    print(p1)
    print(p1.salary)