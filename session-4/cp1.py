class Animal(object):

    def __init__(self, name):
        self.name = name


class Caine(Animal):
    def bark(self):
        print(f'Bark Bark {self.name}')


catzel = Caine('Tasha')
catzel.bark()
