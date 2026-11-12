
import flet as ft
import shop
import menu
import combat

def main(page: ft.Page):
    page.title = "Mitt äventyr"

    player = {
        "gold": 10,
        "health": 100,
        "strength": 34,
        "weapon": 10,
        "experience": 0
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

    def show_bridge(e):
        page.clean()

        page.add(
        ft.Text("Bron över den mörka ravinen", size=30),
        ft.Text("Du kommer fram till en gammal träbro."),
        ft.Text("Plötsligt kliver ett stort troll fram och blockerar vägen!"),
        ft.Text("Trollet ryter: Ingen passerar min bro!"),
        ft.Text("Vad vill du göra?"),
        ft.Button("Slåss mot trollet", on_click=fight),
        ft.Button("Tillbaka till byn", on_click=show_village)
    )


    def fight(e):
     if player["health"] > 0:
        player["health"], player["experience"] = combat.Fight(
            player["health"],
            player["strength"],
            player["weapon"],
            player["experience"]
        )
     if player["health"] <= 0:
        page.clean()
        page.add(
            ft.Text("Du har förlorat!", size=30),
            ft.Text("Du orkade inte besegra trollet."),
            ft.Button("Tillbaka till byn", on_click=show_village)
        )
     else:
         page.clean()
         page.add(
              ft.Text("Striden mot trollet!", size=30),
            ft.Text("Du attackerar trollet!"),
            ft.Text("Din hälsa: " + str(player["health"])),
            ft.Text("Din erfarenhet: " + str(player["experience"])),
            ft.Button("Slåss igen", on_click=fight),
            ft.Button("Tillbaka till bron", on_click=show_bridge)
         )
        
         

        

        
    

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
            ft.Button("Gå mot bron", on_click=show_bridge),
            ft.Button("Meny", on_click=show_menu)
        )

    show_village()

ft.run(main)
