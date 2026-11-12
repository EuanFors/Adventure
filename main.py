import shop
import menu

player = {"gold": 10, "health": 100, "strength": 34}

counter = 0
current_scene = "village"

player["strength"], counter = shop.LearningAcademy(player["strength"], counter)

print(counter, ": Nu är min strength:", player["strength"])

menu.Menu()

player["strength"], counter = shop.LearningAcademy(player["strength"], counter)

print(counter, ": Nu är min strength:", player["strength"])

print("Gold:", player["gold"])
print("Health:", player["health"])
print("Strength:", player["strength"])