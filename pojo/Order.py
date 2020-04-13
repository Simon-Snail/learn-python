class Order(object):

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

    def __init__(self, name):
        self.__product = name


    def toString(self):
        print(f'orderCode:{self.__orderCode}, product:{self.__product}, number:{self.__number}')

order = Order()
order.set_orderCode(13672674127)
order.set_product('ali小蜜')
order.set_number(1)
print(order.__dict__)
