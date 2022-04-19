"""main module"""


class CustomMeta(type):
    """main meta class"""
    def __new__(cls, name, bases, classdict):
        attrs = ((name, value) for name, value in classdict.items() if
                 not (name.startswith('__') and name.endswith('__')))
        custom_attr = dict(("custom_" + name, value) for name, value in attrs)
        attrs = ((name, value) for name, value in classdict.items() if
                 (name.startswith('__')) and name.endswith('__'))
        custom_attr.update(attrs)
        return super().__new__(cls, name, bases, custom_attr)


class Cl(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"

    def __setattr__(self, key, value):
        print("setattr using C")
        new_name = "custom_" + key
        return super().__setattr__(new_name, value)


C = Cl()
print(Cl.__dict__)
print(C.__dict__)
