class Animal:
    def __init__(self, attrs): # нет требовний как задаются атрибутты экземпляров класса
        self.attributes = attrs
    

    def eat(self):
        print("Ate some food!")


class Cat(Animal):
    def eat(self, amount = 0.1): # дополнительный аргумент amount которого нет в родительском классе 
        if amount > 0.3:
            print("Can't eat that much!")
        else:
            print("Ate some cat food!")
    

class Dog(Animal):
    def eat(self):
        print("Ate some dog food!")


pluto = Dog({'name': 'Pluto', 'age': 3})
goofy = Dog({'name': 'Goofy', 'age': 2}) # в одном случае передается словарь
buttons = Cat(('Mr. Buttons', 4)) # в другом кортедж

animals = (pluto, goofy, buttons)

for animal in animals: # для нахождения определенного возраста подойдут не все объекты
    if animal.attributes['age'] > 2:
        print(animal.attributes['name'])
