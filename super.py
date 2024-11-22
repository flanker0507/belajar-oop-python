class Hero:

    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print(f"{self.name} dengan helath: {self.health}")

class Hero_intekgence(Hero):
    def __init__(self,name):
        super().__init__(name, 100)
        super().showInfo()
        # Hero.__init__(self,name,100)


class Hero_strength(Hero):
    def __init__(self,name):
        super().__init__(name,69)
        super().showInfo()
        # Hero.__init__(self,name,100)


lina = Hero_intekgence("lina")
axe = Hero_strength("axe")
print(lina.name , " ", lina.health)
print(axe.name , " ", axe.health)