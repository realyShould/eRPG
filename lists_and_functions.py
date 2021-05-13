import random, os, colorama
from colorama import Fore, Back, Style

colorama.init()

class Player():
    def __init__(self):
        self.right_now_hp = self.default_hp + self.armor
        self.default_hp = 100
        self.armor = 0
        self.right_now_atk = self.default_atk + self.additional_atk
        self.default_atk = 20
        self.additional_atk = 0
        self.coins = 0
        self.heal_count = 0
        self.heal_atr = 50
    def output_status(self):
        print(f'Hp >>> {self.right_now_hp}\nArmor >>> {self.armor}\nAttack >>> {self.right_now_atk}\nWeapon >>> {self.additional_atk}')
    def heal(self):
        if self.heal_count > 0:
            self.right_now_hp += self.heal_atr
            self.heal_count -= 1
            if self.right_now_hp > self.default_hp + self.armor:
                self.right_now_hp = self.default_hp + self.armor
        else:
            print(f'You don\'t have poitions')

    def update(self):
        pass
    armor_inventory = []
    weapon_inventory = []
class Wolf():
    def __init__(self, player):
        self.hp = 30
        self.right_now_hp = self.hp
        self.atk = 10
    def fight(self, player):
        player.right_now_hp -= random.randint(1, self.atk)
        self.right_now_hp -= random.randint(1, player.right_now_atk)
        print(f'Your HP:{player.right_now_hp}\nEnemy HP:{self.right_now_hp}\n'+ str(10 * '='))
        if self.right_now_hp <= 0:
            self.right_now_hp = self.hp
            player.coins += random.randint(1,20)
            print(f'\tYou won!')
        if player.right_now_hp <= 0:
            print(f'\tLose!')
            player.__init__()
        self.fight(player)

class Bear():
    def __init__(self):
        self.hp = 50
        self.right_now_hp = self.hp
        self.atk = 20
    def fight(self, player):
        player.right_now_hp -= random.randint(1, self.atk)
        self.right_now_hp -= random.randint(1, player.right_now_atk)
        print(f'Your HP:{player.right_now_hp}\nEnemy HP:{self.right_now_hp}\n'+ str(10 * '='))
        if self.right_now_hp <= 0:
            self.right_now_hp = self.hp
            player.coins += random.randint(1,30)
            print(f'\tYou won!')
        if player.right_now_hp <= 0:
            print(f'\tLose!')
            player.__init__()
        self.fight(player)

shopItems=[
    'Easy Armor',
    'Medium Armor',
    'Hard Armor',
    'Health poition',
    'Wooden Sword',
    'Stone Sword',
    'Iron Sword'
]

shopItemsPrice={
    'Easy Armor' : 50,
    'Medium Armor' : 100,
    'Hard Armor' : 200,
    'Health poition' : 15,
    'Wooden Sword' : 20,
    'Stone Sword' : 50,
    'Iron Sword' : 100
}

shopItemsAgil={
    'Easy Armor' : 50,
    'Medium Armor' : 100,
    'Hard Armor' : 200,
    'Health poition': 50,
    'Wooden Sword' : 10,
    'Stone Sword' : 30,
    'Iron Sword' : 50
}

listOfEnemy=[
    'wolf',
    'bear'
]
