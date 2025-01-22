from page import Page
from category import Category


class CategoryPage(Page):
    def __init__(self, database, router):
        self.database = database
        self.router = router
        self.state = {}

    def changes(self, parameters):
        pass

    def execute(self):
        while True:
            choice = self.prompt()
            if choice == 4:
                break
            match choice:
                case 1:
                    self.list_categories()
                case 2:
                    self.add_category()
                case 3:
                    self.delete_category()
                case _:
                    print("Invalid choice")
                    self.prompt()
        self.router.back()

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
            if choice not in range(1, 5):
                choice = None
                print("Invalid choice")
        return choice

    def add_category(self):
        name = None
        description = None
        while name is None:
            name = input("Name: ")

        while description is None:
            description = input("Description: ")

        category = Category(-1, name, description)
        self.database.category.insert(category)

    def delete_category(self):
        id = None
        print("Enter -1 to cancel")
        while id is None:
            id = input("Id: ")
            try:
                id = int(id)
            except ValueError:
                id = None
                print("Invalid id")
            if id == -1:
                return
            if id is not None and self.database.category.find_by_id(id) is None:
                id = None
                print("Category not found")
        self.database.category.delete(id)

    def list_categories(self):
        categories = self.database.category.find_all()
        print("Categories")
        print("----------")
        for category in categories:
            print(f"{category.id} {category.name}")
