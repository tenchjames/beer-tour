from page import Page


class CategoryPage(Page):
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
                print("list categories")
            case 2:
                print("add category")
            case 3:
                print("delete category")
            case 4:
                print("back")
                self.router.back()
            case _:
                print("Invalid choice")
                self.prompt()

    def prompt(self):
        print("Category Menu")
        print("1. List Categories")
        print("2. Add Category")
        print("3. Delete Category")
        print("4. Back")
        print()

        choice = None
        while not choice:
            choice = input("Choice: ")
            try:
                choice = int(choice)
            except ValueError:
                choice = None
                print("Invalid choice")

        return choice
