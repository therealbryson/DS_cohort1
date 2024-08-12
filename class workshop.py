class Vehnicle:
    def __init__(self, brand,model,year,color):
        self.brand=brand
        self.model=model
        self.year=year
        self.color=color
    def start(self):
        print('Engine start')
    def park(self):
        print('Car park properly,Engine stop')
    def general_p(self):
        print(f'The car is{self.brand} {self.model} produced in{self.year} and it is {self.color} color')
         
class Car (Vehnicle):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year, color)

    def wheel (self):
        print('The car has four wheels')

car1=Car('Toyota','Camry',2018,'Black')
car1.general_p()
car1.wheel()

#POLYMORPHISM

class Vehnicle:
    def __init__(self,brand,model,year,color):
        self.brand=brand
        self.model=model
        self.year=year
        self.color=color

        
    