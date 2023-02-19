class Dough:
    def __init__(self,flour_type: str, baking_technique: str, weight: float ):
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight

    @property
    def flour_type(self):
        return  self.__flour_type

    @flour_type.setter
    def flour_type(self, value):
        if not value:
            raise ValueError("The flour type cannot be an empty string")
        self.__flour_type = value
    @property
    def baking_technique(self):
        return self.__baking_technique
    
    @baking_technique.setter
    def baking_technique(self, value):
        if not  value:
            raise ValueError("The baking technique cannot be an empty string")
        self.__baking_technique = value
    
    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight = value

# d1= Dough('round','oven', 2.5)
# d2= Dough('','oven', 2.5)
# d3= Dough('round','', 2.5)
# d4= Dough('round','oven', 0)

# print(d1.flour_type)
# print(d1.baking_technique)
# print(d1.weight)
# print(d2.flour_type)
# print(d2.baking_technique)
# print(d2.weight)
# print(d3.flour_type)
# print(d3.baking_technique)
# print(d3.weight)
# print(d4.flour_type)
# print(d4.baking_technique)
# print(d4.weight)


    



