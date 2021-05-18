from datetime import date, datetime


class CellPhone:
    def __init__(self, brand, color, size, price=0.00, date_of_manufacture=None):
        self.brand = brand
        self.size = size
        self.price = price
        self.color = color
        # if date_of_manufacture:
        #     self.date_of_manufacture = date_of_manufacture
        # else:
        #     self.date_of_manufacture = date.today()
        self.date_of_manufacture = date_of_manufacture if date_of_manufacture is not None else date.today() # 三元表达式

    def on(self):
        print('价值{}元的{}颜色的{}品牌的手机开了'.format(self.price, self.color, self.brand))

    def off(self):
        print('价值{}元的{}颜色的{}品牌的手机关了'.format(self.price, self.color, self.brand))

    def send_message(self, number, message=None):
        print('给{}发送了一条短信，内容是{}'.format(number, message))

    def __repr__(self):
        return '<手机 {} {}>'.format(self.brand, self.price)

    def __str__(self):
        return '<手机 {} {} {}>'.format(self.brand, self.price, self.size)

    def __add__(self, other):
        return self.price + other.price

if __name__ == '__main__':
    c1 = CellPhone('iPhone6s', 'golden', 4.7, 5888.00)
    c2 = CellPhone('小米6', '黑色', 5.5, 2999)
    print(c2)
    # print(c1.brand)
    # print(c1.price)
    # print(c1.date_of_manufacture)
    # c1.on()
    # c1.send_message(18301307050, '早点睡觉')
    # c1.off()

    # print('-'*30)
    # c2 = CellPhone('小米6', 'black', 5.5, 2999, date(2017,7,31))
    # print(c2.price)
    # print(c2.brand)
    # print(c2.date_of_manufacture)
    # c2.on()
    # c2.off()