import random, os, colorama
from colorama import Fore, Back, Style

colorama.init()

class Player():
    def __init__(self):
        self.default_hp = 100
        self.armor = 0
        self.right_now_hp = self.default_hp + self.armor
        self.default_atk = 20
        self.additional_atk = 0
        self.right_now_atk = self.default_atk + self.additional_atk
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
            userCommand(player, wolf, bear)
        self.fight(player)

class Bear():
    def __init__(self, player):
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
            userCommand(player, wolf, bear)
        self.fight(player)

player = Player()
wolf = Wolf(player)
bear = Bear(player)



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

def random_opponent(wolf, player, bear):
    enemy = random.choice(listOfEnemy)
    if enemy == 'wolf':
        wolf.fight(player)
        userCommand(player, wolf, bear)
    else:
        bear.fight(player)
        userCommand(player, wolf, bear)

def shop(player):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'[1]',shopItems[0],' ',str(shopItemsPrice[shopItems[0]]))
    print(f'[2]',shopItems[1],' ',str(shopItemsPrice[shopItems[1]]))
    print(f'[3]',shopItems[2],' ',str(shopItemsPrice[shopItems[2]]))
    print(f'[4]',shopItems[3],' ',str(shopItemsPrice[shopItems[3]]))
    print(f'[5]',shopItems[4],' ',str(shopItemsPrice[shopItems[4]]))
    print(f'[6]',shopItems[5],' ',str(shopItemsPrice[shopItems[5]]))
    print(f'[7]',shopItems[6],' ',str(shopItemsPrice[shopItems[6]]))
    print(f'or [exit]')
    userShop=input('shop:')
    userShop=userShop.strip()
    userShop=userShop.lower()
    if userShop=='':
        shop()
    elif userShop=='exit':
        userCommand(player)
    elif userShop == '1' and player.coins >= shopItemsPrice[shopItems[0]]:
        if 'Easy Armor' in player.armor_inventory:
            shop()
        else:
            player.armor_inventory.append(str(shopItems[int(userShop)-1]))
            player.coins-=shopItemsPrice[shopItems[0]]
            player.updateStatus_f()
            shop()
    elif userShop == '2' and player.coins >= shopItemsPrice[shopItems[1]]:
        if 'Medium Armor' in player.armor_inventory:
            shop()
        else:
            player.armor_inventory.append(str(shopItems[int(userShop)-1]))
            player.coins-=shopItemsPrice[shopItems[0]]
            player.updateStatus_f()
            shop()
    elif userShop == '3' and player.coins >= shopItemsPrice[shopItems[2]]:
        if 'Hard Armor' in player.armor_inventory:
            shop()
        else:
            player.armor_inventory.append(str(shopItems[int(userShop)-1]))
            player.coins-=shopItemsPrice[shopItems[0]]
            player.updateStatus_f()
            shop()
    elif userShop == '4' and player.coins >= shopItemsPrice[shopItems[3]]:
        player.healC+=1
        player.coins-=shopItemsPrice[shopItems[0]]
        player.updateStatus_f()
        shop()
    elif userShop == '5' and player.coins >= shopItemsPrice[shopItems[4]]:
        if 'Wooden Sword' in player.weapon_inventory:
            shop()
        else:
            player.weapon_inventory.append(str(shopItems[int(userShop)-1]))
            player.coins-=shopItemsPrice[shopItems[0]]
            player.updateStatus_f()
            shop()
    elif userShop == '6' and player.coins >= shopItemsPrice[shopItems[5]]:
        if 'Stone Sword' in player.weapon_inventory:
            shop()
        else:
            player.weapon_inventory.append(str(shopItems[int(userShop)-1]))
            player.coins-=shopItemsPrice[shopItems[0]]
            player.updateStatus_f()
            shop()
    elif userShop == '7' and player.coins >= shopItemsPrice[shopItems[6]]:
        if 'Iron Sword' in player.weapon_inventory:
            shop()
        else:
            player.weapon_inventory.append(str(shopItems[int(userShop)-1]))
            player.coins-=shopItemsPrice[shopItems[0]]
            player.updateStatus_f()
            shop()
    else:
        print(f'\tError. Restart!')
        player.updateStatus_f()
        shop()

def hunt_f(player, wolf, bear):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n\tWho is your enemy?')
    print('[1]Wolf\n[2]Bear\n[rand]Random(dont work)')
    opponent=input('input:').strip().lower()
    if opponent == '':
        hunt_f()
    elif opponent == '1':
        wolf.fight(player)
    elif opponent == '2':
        bear.fight(player)
    elif opponent == 'rand':
        random_opponent(wolf, player, bear)
        userCommand(player, wolf, bear)
    else:
        print('Such an opponent does not exist or there was an error in the code, for the second option, contact the developer. Repeat.')
        hunt_f()
    userCommand(player)

def userCommand(player, wolf, bear):
    ##os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED,'\t\tHelper')
    print(Fore.CYAN,'hunt - hunting')
    print(Fore.CYAN,'shop - shop')
    print(Fore.CYAN,'heal - heal your character')
    print(Fore.CYAN,'inventory or inv - inventory')
    print(Fore.CYAN,'stats')
    print(Fore.CYAN,'exit')
    print(Fore.MAGENTA)
    userCommand=input('input:').strip().lower()
    if userCommand == '':
        userCommand()
    elif userCommand == 'shop':
        shop()
    elif userCommand == 'hunt':
        hunt_f(player, wolf, bear)
    elif userCommand=='stats' or userCommand == 'status':
        player.output_status()
        userCommand()
    elif userCommand=='exit':
        quit()
    elif userCommand=='inventory' or userCommand == 'inv':
        print(Style.RESET_ALL,Fore.CYAN,'\tYour armor:\n')
        print(player.armor_inventory)
        print('\n\tYour weapons:\n')
        print(player.weapon_inventory)
        print('\n\tHealth poitions:')
        print(str(player.heal_count))
        userCommand()
    elif userCommand == 'heal':
        player.heal()
        userCommand()
    else:
        print('You entered the wrong command or there was an error in your code. In the case of the latter, contact the developer. Restart.')
        userCommand() 