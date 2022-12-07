import csv

def get_csv_data(filename):
    rows = [] #声明一个list列表存放测试数据
    with open(filename,'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            rows.append([int(x) for x in row])#把遍历每一个行得到的结果转换成int类型

    return rows