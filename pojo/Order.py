class Order(object):

    name = 'order'

    @property
    def get_orderCode(self):
        return self.__orderCode

    def set_orderCode(self, orderCode):
        self.__orderCode = orderCode

    def get_product(self):
        return self.__product

    def set_product(self, product):
        self.__product = product

    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number

    def __init__(self, index):
        self.i = index

    def toString(self):
        print(f'orderCode:{self.__orderCode}, product:{self.__product}, number:{self.__number}')

    def __getattr__(self, attr):
        print('not find')





order = Order(1)
order.set_orderCode(13672674127)
order.set_product('ali小蜜')
order.set_number(1)

print(order.get_orderCode)
print(hasattr(order, 'toString'))
print(order.age)
