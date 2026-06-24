from Enemy import *
import random

class Zombie(Enemy):

    def __init__(self, health, damage):
        super().__init__(type_of_enemy='Zombie', health=health, damage=damage)

    def talk(self):
        print(f'{self.get_type_of_enemy()} is grumbling..')

    def spread_disease(self):
        print("Zombie is spreading infection!")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.5
        if did_special_attack_work:
            self.health += 2
            print('Zombie special attack worked and health has been increased by 2 points.')