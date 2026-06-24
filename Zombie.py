from Enemy import *

class Zombie(Enemy):

    def __init__(self, health, damage):
        super().__init__(type_of_enemy='Zombie', health=health, damage=damage)

    def talk(self):
        print(f'{self.get_type_of_enemy()} is grumbling..')

    def spread_disease(self):
        print("Zombie is spreading infection!")