class Student(object):

    count = 0

    def __init__(self, name, sxt, age):
        self._name = name
        self.sxt = sxt
        self.__age = age
        Student.count += 1

    @property
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_set(self):
        return self.sxt

    def set_sxt(self, sxt):
        self.sxt = sxt

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def toString(self):
        print(f'name: {self._name}, sxt: {self.sxt}, age: {self.__age}')


student = Student('xiaoming', 'nan', 20)
print(student._Student__age)
print(student.__dir__())