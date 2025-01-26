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
                self.router.navigate(Pages.TASTINGS)
            case 2:
                self.router.navigate(Pages.PERSON)
            case 3:
                self.router.navigate(Pages.CATEGORY)
            case 4:
                self.router.navigate(Pages.BREWERY)
            case 5:
                self.router.navigate(Pages.BEERS)
            case 0:
                print("exiting...")
                self.router.navigate(Pages.EXIT)
            case _:
                print("Invalid choice")
                self.prompt()

    def prompt(self):
        choice = None
        while choice is None:
            print()
            print("Main Menu")
            print("0. Exit")
            print("1. Drink History")
            print("2. Person Admin")
            print("3. Category Admin")
            print("4. Brewery Admin")
            print("5. Beer Admin")
            print()
            try:
                choice = int(input("Choice: "))
            except ValueError:
                print("Invalid choice")
                choice = None

        return choice
