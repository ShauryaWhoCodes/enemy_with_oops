class Enemy:

    def __init__(self, type_of_enemy, health, damage):
        self.__type_of_enemy = type_of_enemy
        self.health = health
        self.damage = damage

    def talk(self):
        print(f'I am {self.__type_of_enemy}, be prepared for a fight! ')

    def attack(self):
        print(f'{self.__type_of_enemy} has attacked for {self.damage} damage!')

    def walk_forward(self):
        print(f'{self.__type_of_enemy} is moving closer to you')

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def special_attack(self):
        print("Enemy doesn't have any special attack")