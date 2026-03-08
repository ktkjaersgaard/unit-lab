from random import randint,seed
from Unit_json_write import Add_unit
import json
class Get_Unit():
    def __init__(self,Unit_1,name):
        weapon = Unit_1["Weapons"]
        weapon = weapon[next(iter(weapon))]
        self.name = name
        self.weapon_atk = weapon["A"]
        self.weapon_bs = weapon["BS"]
        self.weapon_str = weapon["S"]
        self.weapon_dmg = weapon["D"]
        self.t =  Unit_1["T"]
        self.w =  Unit_1["W"]
        self.s =  Unit_1["SV"]
        print("\n")
    def hit(self,t):
        self.wounds = 0
        for i in range(0,self.weapon_atk):
            seed(randint(0,1000000000000))
            if d6() >= self.weapon_bs:
                if self.weapon_str <= t/2:
                    diff = 6
                elif self.weapon_str == t:
                    diff = 4
                elif self.weapon_str >= t*2:
                    diff = 2
                elif self.weapon_str >= t+1:
                    diff = 3
                else:
                    diff = 5
                if d6() >= diff:
                    self.wounds = self.wounds+1
        return self.wounds
    def save(self,wounds,dmg):
        for i in range(0,wounds):
            if d6() <= self.s:
                self.w = self.w - dmg
        if self.w > 0:
            print(f"{self.name} wounds is at",self.w)
        else:
            print(f"{self.name} is dead")
def main():
    print("1: Add a unit\n2: Battle two units")
    if input("") == "1":
        Add_unit()
    else:
        arena()
def Get_unit_data():
    with open("units.json", "r") as file:
        units = json.load(file)
        for name in units:
            print(name+"\n")
        n1 = input("Unit 1: ").lower()
        n2 = input("Unit 2: ").lower()
        return units[n1] , units[n2], n1,n2
    print("pick 2 units\n")
    for name in units:
        print(name+"\n")
def arena(Unit_1=False,Unit_2=False,n1=False,n2=False):
    if not Unit_1:
        Unit_1, Unit_2, n1, n2 = Get_unit_data()
    fighter = Get_Unit(Unit_1,n1)
    defender = Get_Unit(Unit_2,n2)
    defender.save(fighter.hit(defender.t),fighter.weapon_dmg)
    again = input("again. (y/n)").lower()
    if again == "y":
        again = input("the same units?(y/n)").lower()
        if again == "y":
            arena(Unit_1=Unit_1,Unit_2=Unit_2,n1=n1,n2=n2)
        arena()
def d6():
    return randint(0,6)

main()