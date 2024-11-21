class Hero:

    # class variable
    jumlah = 0
    __privateJumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        # variable instance private
        self.__private__ = "private"

        # variable instance protected
        self._protected = "protected"

dilla = Hero("Dilla",100)

print(dilla.__dict__)
print(dilla.health)
print(dilla.__private__)