class Animal(object):
    def __init__(self, name, age):
        """Constructor"""
        self._name = name
        self._age = age

    def __del__(self):
        print(f'Bye bye {self._name}')

    def say_hi(self):
        print(f'Hello, my name is {self._name}')


a1 = Animal('Tasha', 2)
a1.say_hi()

a2 = Animal('Thor', 2)
a2.say_hi()

del a1
