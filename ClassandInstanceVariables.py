class Hero: # Template
    # Class Variable
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # Instance Variable
        self.Name = inputName
        self.Health = inputHealth
        self.Power = inputPower
        self.Armor = inputArmor
        Hero.jumlah += 1
        print("Membuat Hero Dengan name" + inputName)

hero1 = Hero("Sniper", 100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("Mirana", 100, 15, 1)
print(Hero.jumlah)
hero3 = Hero("Ucup", 1000, 69,69)
print(Hero.jumlah)

