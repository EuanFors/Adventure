
import flet as ft
import shop
import menu

def main(page: ft.Page):
    page.title = "Mitt äventyr"

    player = {
        "gold": 10,
        "health": 100,
        "strength": 34
    }

    counter = 0

    def train(e):
        nonlocal counter

        player["strength"], counter = shop.LearningAcademy(
            player["strength"], counter
        )

        show_village()

    def show_menu(e=None):
        page.clean()

        page.add(
            ft.Text("Meny", size=30),
            ft.Text("Välkommen till äventyret!"),
            ft.Button("Tillbaka till byn", on_click=show_village)
        )

    def show_shop(e):
        page.clean()

        page.add(
            ft.Text("Affären", size=30),
            ft.Text("Välkommen till affären!"),
            ft.Text("Gold: " + str(player["gold"])),
            ft.Button("Köp hälsodryck (5 guld)", on_click=buy_potion),
            ft.Button("Tillbaka till byn", on_click=show_village)
        )

    def buy_potion(e):
        if player["gold"] >= 5:
            player["gold"] = player["gold"] - 5
            player["health"] = player["health"] + 20

        show_shop(e)

    def show_village(e=None):
        page.clean()

        page.add(
            ft.Text("Välkommen till byn!", size=30),
            ft.Text("Vad vill du göra?"),
            ft.Text("Strength: " + str(player["strength"])),
            ft.Text("Gold: " + str(player["gold"])),
            ft.Text("Health: " + str(player["health"])),
            ft.Button("Träna", on_click=train),
            ft.Button("Affären", on_click=show_shop),
            ft.Button("Meny", on_click=show_menu)
        )

    show_village()

ft.run(main)
