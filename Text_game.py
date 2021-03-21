import random
default_attack=["Punched","Slashed","Stabbed","shot"]

class person:
    def __init__(self,hp):
        self.type_of_attack=random.choice(default_attack)
        self.hp = hp
        self.attack_damage=random.randint(5,12)
    def attack(self,monster):
        monster.hp -= self.attack_damage
        print(f"You have {self.type_of_attack} the monster for {self.attack_damage}. The monster is now left it {monster.hp}")
    def heal(self):
        if self.hp<20:
            amout_of_heal=random.randint(4,12)
            self.hp += amout_of_heal
            print(f"You now have healed yourself for {amout_of_heal} HP, you now have {self.hp}")
        else:
            print(f"You have {self.hp} HP, heal only works when you are below 20HP. ")
    def run(self):
        chance=random.randint(1,2)
        if chance==1:
            print(f"You have escaped the monster")
        else:
            print(f"You have not escapped the monsters")
class fighter(person):
    def talent(self,monster):
        chance=random.randint(1, 8)
        if chance==1:
            monster.hp-=40
            print(f"You have landed the final strike. The gods have hit the monster for 40 damage. Leaving him with {monster.hp} HP left.")
        else:
            damage=random.randint(6 , 13)
            self.hp-=damage
            print(f"You have displeased the gods. They have striked for {damage}. You are left with {self.hp} HP")

class wizard(person):
    def talent(self,monster):
        amout_of_shots=random.randint(1, 3)
        damage=2*amout_of_shots
        monster.hp-=damage
        print(f"{amout_of_shots} fireballs have hit the monster hit him for {damage}. Leaving the monster with {monster.hp} HP.")

class monster:
    def __init__(self,hp,attack):
        self.hp=hp
        self.attack=attack
        self.attack_damage=random.randint(1,9)
    def monster_attack(self,player):
        player.hp -= self.attack_damage
        print(f"You have been damage from the monster for {self.attack_damage}. You are left with {player.hp} ")
    def monster_heal(self):
        self.hp += random.randint(1, 5)
        print(f"The monster used heal it now has {self.hp} HP,")
class dragon(monster):
    def flame_blast(self,player):
        for turns in range(0, 3):
            damage=random.randint(3,8)
            player.hp-=damage
            print(f"The dragon has burned you for {damage}.Leaveing with {player.hp}")
def monster_opoions(monster,player):
    monster_special_attack_chance = random.randint(1, 5)
    if monster.hp < 5:
        monster.monster_heal()
    elif monster_special_attack_chance == 1:
        monster.flame_blast(player)
    else:
        monster.monster_attack(player)
def main():
    player = None
    player_wizard = wizard(30)
    player_fighter = fighter(40)
    monster = dragon(10, "Slash")
    print("Welcome to dungeon!"
          "\n Here is a quick run down"
          "\n There are 2 classes: Fighter and Wizard"
          "\n Wizard talents: Fireball does 5 damage * the amount of shots. Chance to burn yourself"
          "\n Fighter talents: Final strike has a 1 in 8 chance to do 40 damage. But a chance to dp 6-13 damage to yourself"
          "\n Everyone has 3 normal ablities. "
          "\n1) Attack, does 5-12 damage. NOTE, always hits and has no negative repercussions "
          "\n2) Heal, heals between 1,7 HP. NOTE, only works when under 20 HP)"
          "\n3) Run, Has a 1/4 chance of running away from the target. Note, if moves fails this does count as a move")
    choose_class=str(input("\nPlease choose a class: Fighter or Wizard.")).lower()
    if choose_class=="fighter":
        player=player_fighter
        print("Congrats on choosing to be the strongest.")
    elif choose_class=="wizard":
        player=player_wizard
        print("Welcome to the wizard club")
    else:
        print("Sorry That is a invalid class.")
        exit()
    while player.hp>0:
        choose_door=str(input("Choose a door 1: 2: 3:"))
        stop_battle = False
        monster.hp=random.randint(23,40)
        if choose_door.isdigit()==False and len(choose_door)!=1:
            print("\nPlease a choose a number 1, 2, 3. Don't put any letters and make sure there is only one digit.")
            break
        while stop_battle==False:
            if monster.hp < 0:
                print("You have slayed the monster")
                stop_battle=True
            elif player.hp<0:
                print("You have died")
                stop_battle=True
            else:
                player_choice = str(input("\nYou open the door and see a monster. What shall you do. Attack: Heal: Run: Talent:")).lower()
                if player_choice == "attack":
                    player.attack(monster)
                    monster_opoions(monster,player)
                elif player_choice == "heal":
                    player.heal()
                    monster_opoions(monster,player)
                elif player_choice == "run":
                    player.run()
                    monster_opoions(monster,player)
                elif player_choice == "talent":
                    player.talent(monster)
                    monster_opoions(monster,player)
main()
