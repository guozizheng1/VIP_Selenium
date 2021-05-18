def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


calculate = (lambda a, b: a * b)  # lambda表达式


if __name__ == '__main__':
    print(calculate(5, 3))
