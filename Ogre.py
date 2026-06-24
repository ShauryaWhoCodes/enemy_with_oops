from Enemy import Enemy

class Ogre(Enemy):

    def __init__(self, health, damage):
        super().__init__(type_of_enemy='Ogre', health=health, damage=damage)

