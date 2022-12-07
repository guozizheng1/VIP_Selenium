import csv


def get_csv_data(filename):
    rows=[]
    with open('D:\\VIP_Selenium\\SEC12\\data\\users.csv','r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            rows.append(row)

    return rows