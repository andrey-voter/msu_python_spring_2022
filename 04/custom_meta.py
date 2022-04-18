"""main module"""


class CustomMeta(type):
    """main meta class"""
    def __new__(cls, name, bases, classdict):
        attrs = ((name, value) for name, value in classdict.items() if not name.startswith('__'))
        custom_attr = dict(("custom_" + name, value) for name, value in attrs)
        attrs = ((name, value) for name, value in classdict.items() if name.startswith('__'))
        custom_attr.update(attrs)
        return super().__new__(cls, name, bases, custom_attr)
