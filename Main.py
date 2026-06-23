from enemy_with_oops.Enemy import *

zombie = Enemy('zombie', 10, 1)
ogre = Enemy('ogre', 6, 15)



zombie.talk()
zombie.walk_forward()
zombie.attack()

ogre.talk()
ogre.walk_forward()
ogre.attack()