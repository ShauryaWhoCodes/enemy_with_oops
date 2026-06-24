from Enemy import Enemy
import random

class Ogre(Enemy):

    def __init__(self, health, damage):
        super().__init__(type_of_enemy='Ogre', health=health, damage=damage)

    def special_attack(self):
        did_special_attack_work = random.random() < 0.2
        if did_special_attack_work:
            self.health += 4
            print('Ogre special attack worked and health has been increased by 4 points.')