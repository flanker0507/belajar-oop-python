import os


class Hero:
    def __init__(self,name,health):
        os.system("clear")
        self.name = name
        self.health = health

    def showInfo(self):
        print("Show Info From Constructor")
        print(f"{self.name} Health: {self.health}")

class Hero_inteligance(Hero):
    def __init__(self,name):
        super().__init__(name,100)

    # override
    def showInfo(self):
        print("Show Info From Hero_inteligance")
        print(f"{self.name} \n\tTipe: inteligence, \n\tHealth: {self.health}")

class Hero_strength(Hero):
    def __init__(self,name):
        super().__init__(name,200)

lina = Hero_inteligance('lina')
axe = Hero_strength('axe')

lina.showInfo()
axe.showInfo()