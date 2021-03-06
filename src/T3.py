# T3.py
# from singleton import SingletonExample


class Person(object):
    def __init__(self):
        print('init')

    @staticmethod
    def sayHello(hi):
        if hi is None:
            hi = 'hello'
        print(hi)

    @classmethod
    def hi(cls, msg):
        print(msg)
        print(dir(cls))

    # 一般类的方法
    def hobby(self, hobby):
        print(hobby)


# 调用静态方法，不用实例化
Person.sayHello('hi')
Person.hi('Hi!')
# Person.sayHello('')
# 实例化类调用普通方法,__init__在这里触发
person = Person()
person.hobby('football')


# print("Singleton!")
# s = SingletonExample()
# print(id(s))