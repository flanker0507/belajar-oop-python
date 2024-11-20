from os import uname


class Hero:
    #class variable
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

    # void function method tanpa return, tanpa ergumen
    def siapa(self):
        print("nama ku adalah " + self.name)

    # method dengan argumen, tanpa return
    def healthUp(self, up):
        self.health += up
        self.power += up

    # method dengan return
    def powerUp(self, up):
        return self.power + up


hero1 = Hero('sniper', 100, 10, 5)
hero2 = Hero('mario bros', 90, 5, 10)

hero1.siapa()
hero2.siapa()

hero1.healthUp(10)
print(hero1.health)

print(hero1.powerUp(10))