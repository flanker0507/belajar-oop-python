# Magic Method
class Mangga:

    def __init__(self,name,jumlah):
        self.name = name
        self.jumlah = jumlah

    def __repr__(self):
        return f"Debug - Mangga: {self.name} dengan jumlah: {self.jumlah}"

    def __str__(self):
        return f"Debug - Mangga: {self.name} dengan jumlah: {self.jumlah}"

    def __add__(self, object):
        return self.jumlah + object.jumlah

    @property
    def __dict__(self):
        return "object ini mempunyai nama dan jumlah"

belaja1 = Mangga("arumanis",69)
belaja2 = Mangga("Kecut",30)
print(belaja1)
print(belaja2)
print(belaja1 + belaja2)
print(belaja1.__dict__)