from exercise_encapsulation.ex_2_pizza_maker.project.dough import Dough
from exercise_encapsulation.ex_2_pizza_maker.project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value

    def add_topping(self, topping: Topping):
        if self.__toppings_capacity == len(self.toppings):
            raise ValueError("Not enough space for another topping")
        if topping in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping] = topping.weight

    def calculate_total_weight(self):
        return self.dough.weight + sum(self.toppings.values())
# p1 = Pizza('Ivan', Dough('ppp','hhhh', 2.5), 5 )


