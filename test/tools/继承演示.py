"""
类的继承:
类:
    执行顺序:
        类属性
        __new__
        __init__
    单例模式:
        类属性:1
        __new__:1
        __init__:1
    调用:
        会执行子类的类属性

子类:
     执行顺序:
        类属性
        __new__
        __init__
    单例模式:
        类属性:1
        __new__:1
        __init__:1
    调用:
        会执行子类的类属性

单例模式:
    父类实例化后,子类会指向父类
"""


class AAAAA(object):
    def __new__(cls, *args, **kwargs) -> object:
        if not hasattr(cls, "_instance"):  # 反射
            cls._instance = object.__new__(cls)
            print("A2: __new__")
        return cls._instance

    def __init__(self, name):
        if not hasattr(self, "_init_flag"):  # 反射
            print("A2: __init__")
            self._init_flag = True  # 只初始化一次
            self.name = name

class BBBBBBB(AAAAA):
    def __init__(self, name):
        super().__init__(name)
        print("C2 : __init__")
        print(self.name)

    def get_name(self):
        print(self.name)


if __name__ == '__main__':
    # aaaa = AAAAA("aaaaaaaaaa")
    # print(id(aaaa))
    # A()
    # B()
    # B()
    # C()
    ccccc = BBBBBBB("bbbbbbbb")
    print(id(ccccc))
    ccccc.get_name()

    ccccc = BBBBBBB("aaaaaaaaaa")
    ccccc.name = "aaaaaaaaaa"
    print(id(ccccc))
    ccccc.get_name()
