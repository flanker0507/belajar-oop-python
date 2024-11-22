class Hero:

    def __init__(self,name,health):
        self.name = name
        self.health = health

class Hero_intelegence(Hero):
    pass

class Hero_strenght(Hero):
    pass

lina = Hero("Lina",69)
techies = Hero_intelegence("Techies",96)
axe = Hero_strenght("Axe",99)

print(lina.name)
print(techies.name)
print(axe.name)