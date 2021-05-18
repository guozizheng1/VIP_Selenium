from datetime import date, datetime

class Employee:
    def __init__(self, name, birthdate, gender, department, salary):
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.department = department
        self.salary = salary

    def working(self):
        print('{} 在工作...'.format(self.name))

    def __repr__(self):
        return '<员工 {} {} {}>'.format(self.name, self.department, self.salary)


class Programmer(Employee):
    def __init__(self, name, birthdate, gender, department, salary, skills, project):
        # self.name = name
        # self.birthdate = birthdate
        # self.gender = gender
        # self.department = department
        # self.salary = salary
        # Employee.__init__(self, name, birthdate, gender, department, salary)
        super(Programmer, self).__init__(name, birthdate, gender, department, salary)
        self.skills = skills
        self.project = project

    def working(self):
        # super.working()
        print('程序员{}在参与{}项目'.format(self.name, self.project))

    def learning(self, language):
        print('{}在学习{}'.format(self.name, language))


class HR(Employee):
    def __init__(self, name, birthdate, gender, department, salary, level):
        super(HR, self).__init__(name, birthdate, gender, department, salary)
        self.level = 1

    def working(self):
        print('人事{}来从事相关工作'.format(self.name))

if __name__ == '__main__':
    # emp = Employee('Tom', date(1990, 3, 3), '男', '财务部', 5000.00)
    # print(emp)
    # emp.working()
    p = Programmer('Jerry', date(1991, 8, 8), '男', '开发部', 25000.00, 'Python', 'mystore')
    print(p)
    p.learning('Django')
    p.working()
    hr = HR('Marry', date(1992, 8, 9), '女', '人力资源部', 7800.00, 1)
    hr.working()