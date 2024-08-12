class Player:
    def __init__(self, name,age ):
        self.name=name
        self.age=age
    def run(self):
        print(f'{self.name}is a player in the team')


class AdvancedPlayer(Player):
    def __init__(self,name,age,skills):
        super().__init__(name,age)
        self.skills=skills

    def run(self):
        print(f'{self.name}is also a {self.skills}')

player1=Player('John' , 25)
player2=AdvancedPlayer('kelvin', 25,'Shot')
player_list=[player1,player2]

for player in player_list:
    player.run()