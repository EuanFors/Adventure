import shop
import menu

strenght = 34 
counter = 0

strenght, counter = shop.LearningAcademy(strenght, counter)
print(counter, ": Nu är min strenght:", strenght, counter)

menu.Menu()

strenght, counter = shop.LearningAcademy(strenght, counter)
print(counter, ": Nu är min strenght:", strenght)



