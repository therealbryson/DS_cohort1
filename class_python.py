# class AnimalClass:
#     name='Dog' # class variable
#     def run(self):
#         print(f'The {self.name} is running')
#     def eat(self, meal):
#         self.meal=meal # instance variable
#         print(f'The {self.name} love eating {self.meal}')


# animal=AnimalClass()
# animal.run()
# animal.eat('Bone')


# class car:
#     def make(self, make_name):
#         self.make_name=make_name
#         print(f'The car is a make of {self.make_name}')

# car1=car()
# car1.make('Toyota')


# class DistanceConverter:
#     kms_per_s=100
#     def checkmile(self, mile):
#         return mile*self.kms_per_s
    
# converter=DistanceConverter()
# km_10_s=converter.checkmile(10)
# print('The distance cover for 10mile is', km_10_s)


# ## Constructor

# class SearchEngine:
#     secure_url='https//:'
#     def __init__(self, url):
#         self.url=url
#     def secure(self):
#         return self.secure_url + self.url
#         # return "{prefix}{site}".format(prefix=self.secure_url,site=self.url)

# browser1=SearchEngine('www.gomycode.com')
# print(browser1.secure())
# # print(browser1.url)
# browser2=SearchEngine('www.wikipedia.com')
# print(browser2.secure())


class Player:
    def _init_(self, name, hp):
        self.name=name
        self.hp=hp
    def run(self):
        print(f'{self.name} run in this game')
    def takedamage(self, damage):
        self.damage=damage
        self.hp=self.hp-self.damage
        print(f'{self.name}, has {self.hp} points after sustaining {self.damage} points damage')

player1=Player('Diamond', 100)
player1.takedamage(20)

class SuperPlayer(Player):
    def __init__(self, name, hp):
       super().__init__(name, hp)
    

    def fly(self):
        print(f'{self .name} is a supper player')


player1=SuperPlayer('John' 100)

















