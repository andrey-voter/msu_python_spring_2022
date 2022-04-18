class Integer:
    def __init__(self, val=0):
        self.val = val

    def __get__(self, obj, objtype):
        print(f'Integer get {obj} cls={objtype}')
        return self.val

    def __set__(self, obj, val):
        print(f'Integer set {val} for {obj}')
        try:
            if isinstance(val, int):
                self.val = val
            else:
                raise ValueError
        except ValueError:
            print("Not integer given \n")


class String:
    def __init__(self, val=''):
        self.val = val

    def __get__(self, obj, objtype):
        print(f'String get {obj} cls={objtype}')
        return self.val

    def __set__(self, obj, val):
        print(f'String set {val} for {obj}')
        try:
            if isinstance(val, str):
                self.val = val
            else:
                raise ValueError
        except ValueError:
            print("Not str given \n")


class PositiveInteger:
    def __init__(self, val=0):
        self.val = val

    def __get__(self, obj, objtype):
        print(f'Integer get {obj} cls={objtype}')
        return self.val

    def __set__(self, obj, val):
        print(f'Positive integer set {val} for {obj}')
        try:
            if isinstance(val, int):
                pass
            else:
                raise ValueError

        except ValueError:
            print("Not integer given \n")
            return

        try:
            if val > 0:
                self.val = val
            else:
                raise ValueError

        except ValueError:
            print("Not positive integer given \n")


class Data:
    num = Integer()
    name = String()
    price = PositiveInteger()


D = Data()
D.num = "aaaaa"
D.num = 5.54

D.price = -12
D.price = 12.24
D.price = -12.24

D.name = 15
D.name = -15
D.name = 4.44
D.name = -4.44
D.name = 0
