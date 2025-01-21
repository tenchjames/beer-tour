from pages import Pages
from page import Page


class MainPage(Page):
    def __init__(self, database, router):
        self.database = database
        self.router = router
        self.state = {}

    def changes(self, parameters):
        pass

    def execute(self):
        choice = self.prompt()
        match choice:
            case 1:
                self.router.navigate(Pages.CATEGORY)
            case 2:
                print("breweries")
            case 3:
                print("locations")
            case 4:
                print("beers")
            case 5:
                print("tastings")
            case 6:
                print("exiting...")
                self.router.navigate(Pages.EXIT)
            case _:
                print("Invalid choice")
                self.prompt()

    def prompt(self):
        choice = None
        while not choice:
            print("Main Menu")
            print("1. Categories")
            print("2. Breweries")
            print("3. Tasting Locations")
            print("4. Beers")
            print("5. Tastings")
            print("6. Exit")
            print()
            try:
                choice = int(input("Choice: "))
            except ValueError:
                print("Invalid choice")
                choice = None

        return choice
