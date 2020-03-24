# 求绝对值
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 空函数
def pop():
    pass


def my_power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#去除前后空格
def my_trim(x):
    if x[0:1] == ' ':
        x = x[1:]
    elif x[-1:] == ' ':
        x = x[:-1]
    else:
        return x
    return my_trim(x)


print(my_abs(-3))
print(my_power(2))
print(my_trim('  asd '))
