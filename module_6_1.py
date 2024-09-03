class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

class Mammal(Animal, Plant):
    def eat(self, food):
        if isinstance(food, Fruit) or isinstance(food, Flower):
            self.edible = True
        if self.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
            return self.fed
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
            return self.alive

class Predator(Animal, Plant):

    def eat(self, food):

        if isinstance(food, Flower) or isinstance(food, Fruit):
            self.edible = False

        if self.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
            return self.fed
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
            return self.alive

class Flower(Plant):
    edible = True

class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)