from page import Page
from category import Category
from util import standard_admin_menu


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
            if choice == 0:
                break
            match choice:
                case 1:
                    self.list()
                case 2:
                    self.add()
                case 3:
                    self.delete()
                case _:
                    print("Invalid choice")
                    self.prompt()
        self.router.back()

    def prompt(self):
        return standard_admin_menu("Category")

    def add(self):
        name = None
        description = None
        while name is None:
            name = input("Name: ")

        while description is None:
            description = input("Description: ")

        category = Category(-1, name, description)
        self.database.category.insert(category)

    def delete(self):
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

    def list(self):
        categories = self.database.category.find_all()
        print("Categories")
        print("----------")
        for category in categories:
            print(f"{category.id}. {category.name}")
