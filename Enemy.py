class Enemy:

    type_of_enemy: str
    health: int = 10
    damage: int = 1

    def talk(self):
        print(f'I am {self.type_of_enemy}, be prepared for a fight! ')

    def attack(self):
        print(f'{self.type_of_enemy} has attacked for {self.damage} damage!')

    def walk_forward(self):
        print(f'{self.type_of_enemy} is moving closer to you')
