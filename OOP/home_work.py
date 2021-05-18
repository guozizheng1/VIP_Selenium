"""
1. 以面向对象型式：公交车
    特征：
        线路
        起点
        终点
        座位数量
        ...
    行为:
        启动()
        停止()
        开门()
        ...
2. 以dict字典表的形式展现
3. 以namedtuple形式展现
4. 以class形式展现
"""


class Bus:
    def __init__(self, line, start, end, seat):
        self.line = line
        self.start = start
        self.end = end
        self.seat = seat

    def startBus(self):
        print('启动公交车')

if __name__ == '__main__':
    bus1 = Bus('海淀-朝阳', '知春路', '望京', 55)
    bus1.startBus()