


'''Higher-order function'''

'变量可以指向函数'
abs(10)

'函数名也是变量'

def createCounter():
    fs = [0]
    num = 1
    def counter():
        num += + 2
        fs[0] = fs[0] + 1
        return 
    return counter

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f'{createCounter()}, {createCounter()}, {createCounter()}')
