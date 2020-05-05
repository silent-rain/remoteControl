class A(object):
    print("A")


class B(object):
    print("B")


class C(object):
    print("C")


class D(object):
    def __init__(self):
        self.obj_list = []

    def main(self):
        self.obj_list.append(A)
        self.obj_list.append(B)
        self.obj_list.append(C)

        for ui in self.obj_list:
            print(ui)
            print(ui.__name__)



if __name__ == '__main__':
    D().main()
