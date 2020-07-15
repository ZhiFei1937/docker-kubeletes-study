"""
元类是类元编程最高级的工具：使用元类可以创建具有某种特质的全新种类，例如抽象基类。
元类：制造类的工厂，是一个类而不是一个函数。
类工厂函数：collections.namedtuple。把一个类名和几个属性名传给这个函数，
           它会创建一个tuple的子类，其中的元素通过名称获取。
"""

def record_factory(cls_name, fieldnames):
    """
    一个简单的类工厂函数，如：
        dog = record_factory('dog', 'name weight owner')
        rex = dog('rex', 30, 'Bob')
    """
    try:
        field_names = fieldnames.replace(',', ' ').split()
    except AttributeError:
        pass
    field_names = tuple(field_names)

    def __init__(self, *args, **kwargs):
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):
        values = ', '.join('{}={!r}'.format(*i) for i in zip(self.__slots__, self))
        return '{}({})'.format(self.__class__.__name__, values)

    cls_attrs = dict(__slots__ = field_names,
                     __init__ = __init__,
                     __iter__ = __iter__,
                     __repr__ = __repr__)
    return type(cls_name, (object,), cls_attrs)
    pass

if __name__ == '__main__':
    from collections import namedtuple
    dog = record_factory('dog', 'name weight owner')
    rex = dog('rex', 30, 'Bob')
    print(rex)