class Car:
    # konstruktor
    def __init__(self, color, engine, spz):
        self.color = color
        self.engine = engine
        self.spz = spz

    def change_color(self, new_color):
        self.color = new_color

    def __repr__(self):
        return 'Color: {}, Engine: {}, SPZ: {}'.format(self.color, self.engine, self.spz)
    
    def __eq__(self, other):
        if isinstance(other, Car):
            return self.spz == other.spz
        return False


car1 = Car('red', 'TSI', '7AE 5487')
car2 = Car('red', 'TSI', '7AE 5487')

print(car1 == car2)
