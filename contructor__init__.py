class Hero:

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.Name = inputName
        self.Health = inputHealth
        self.Power = inputPower
        self.Armor = inputArmor

hero1 = Hero("Sniper", 100, 10, 4)
hero2 = Hero("Mirana", 100, 15, 1)
hero3 = Hero("Ucup", 1000, 69,69)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)

print(hero1.Name)