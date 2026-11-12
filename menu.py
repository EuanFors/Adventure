def Menu():
    print("Välkommen till affären!")
    print("1. Köp ett svärd")
    print("2. Köp en hälsodryck")
    print("3. Gå tillbaka")

    choice = input("Vad vill du göra? ")

    if choice == "1":
        print("Du har valt att köpa ett svärd!")
    elif choice == "2":
        print("Du har valt att köpa en hälsodryck!")
    elif choice == "3":
        print("Du lämnar affären.")
    else:
        print("Ogiltigt val!")