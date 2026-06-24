from enemy_with_oops.Enemy import *
from Zombie import Zombie
from Ogre import Ogre

zombie = Zombie(health=20, damage=5)
ogre = Ogre(health=20, damage=5)

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health > 0 and e2.health > 0:
        print('-------------------')
        e1.special_attack()
        e2.special_attack()
        # attack by ogre
        e2.attack()
        e1.health -= e2.damage
        e1.attack()
        e2.health -= e1.damage
        print(f"{e1.get_type_of_enemy()} health: {e1.health}")
        print(f"{e2.get_type_of_enemy()} health: {e2.health}")

    if e1.health >= e2.health:
        print(f"Congratulations 🥳, {e1.get_type_of_enemy()} wins! 🥳")
    else:
        print(f"Congratulations 🥳, {e2.get_type_of_enemy()} wins! 🥳")


battle(zombie, ogre)
