class Person:
    def __init__(self, identification, name, age):
        self.identification = identification
        self.name = name
        self.age = age

    def __str__(self):
        return 'Name: {0}, Age: {1}'.format(self.name, self.age)

    def __eq__(self, other):
        return self.identification == other.identification

    @staticmethod
    def sum(x, y):
        return x + y

    def greet(self):
        print('Ahoj', self.name)

    @classmethod
    def sum(x, y):
        return x + y


p1 = Person(1234, 'Honza', 20)
p2 = Person(12345, 'Jirka', 70)
p3 = Person(1234, 'Honza', 20)

print(Person.sum(1, 2))
p1.greet()
print(p1.sum(1, 2))

print(p1 == p3)
print(1 == 3)


a = int(input('Zadejte cislo v rozsahu 10 až 100:'))
if not 10 < a < 100:
    raise ValueError('Není v rozsahu 10 až 100')


