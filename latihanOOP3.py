from Hero import HeroInteligence, HeroStrength, Hero

# Membuat Objek Langsung dari Kelas Hero
generic_hero = Hero("Default Hero")
generic_hero.levelUp = 1  # Set level ke 1
generic_hero.show_info()  # Tampilkan informasi hero

lina = HeroInteligence('lina')
slardar = HeroStrength('slardar')

lina.show_info()
slardar.show_info()

# lina.gainExp = 200
# slardar.gainExp = 250
#
# lina.show_info()
# slardar.show_info()

