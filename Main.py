from enemy_with_oops.Enemy import *
from Zombie import Zombie
from Ogre import Ogre

zombie = Zombie(health=10, damage=10)


print("Enemy 1 is ready...")
zombie.talk()
zombie.walk_forward()
zombie.attack()
zombie.spread_disease()

print()
print("Enemy 2 is also ready....")
ogre = Ogre(health=20, damage=20)
ogre.talk()
ogre.walk_forward()
ogre.attack()