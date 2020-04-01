# 函数的参数类型
# 1.位置参数 必须有且仅有括号里的参数


def my_test(x):
    return x * x


# 2.默认参数
def my_test2(x, n=2):
    return x * n


print(my_test2(3, 3))
# 3.可变参数，在前面加*，在函数内部，参数numbers接收到的是一个tuple，调用该函数时，可以传入任意个参数，包括0个参数：


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# 4.关键字参数 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

#5.命名关键字参数

# *********************************************************************************************

def product(*nums):
    num = 1
    for n in nums:
        num = num * n
    return num

def test(name, *, ages):
    return name, ages
print(product(product(1,2,3)))
s = '112314'
print(int(s))
print(test('小明', ages = 1))
