from page import Page
from beer import Beer
from util import standard_admin_menu, get_text_input


class BeerPage(Page):
    def __init__(self, database, router):
        self.database = database
        self.repository = database.beer
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
                case 4:
                    self.list_by_brewery()
                case _:
                    print("Invalid choice")
                    self.prompt()
        self.router.back()

    def prompt(self):
        print()
        print("Beer Menu")
        print("0. Back")
        print("1. List")
        print("2. Create")
        print("3. Delete")
        print("4. List by brewery")
        print()
        choice = None
        while choice is None:
            choice = input("Choice: ")
            try:
                choice = int(choice)
            except ValueError:
                choice = None
                print("Invalid choice")
        return choice

    def _get_brewery_id(self):
        brewery_id = None
        breweries = self.database.brewery.find_all()
        for i in range(len(breweries)):
            brewery = breweries[i]
            brewery_name = brewery.name
            print(f"{i}. {brewery_name}")
        while True:
            choice = input("Brewery: ")
            try:
                choice = int(choice)
            except ValueError:
                choice = None
                print("Invalid choice")
                continue
            if choice < 0 or choice >= len(breweries):
                print("Invalid choice")
                continue
            brewery = breweries[choice]
            brewery_id = brewery.id
            break
        return brewery_id

    def _get_category_id(self):
        category_id = None
        categories = self.database.category.find_all()
        for i in range(len(categories)):
            category = categories[i]
            category_name = category.name
            print(f"{i}. {category_name}")

        while True:
            choice = input("Category: ")
            try:
                choice = int(choice)
            except ValueError:
                choice = None
                print("Invalid choice")
                continue
            if choice < 0 or choice >= len(categories):
                print("Invalid choice")
                continue
            category = categories[choice]
            category_id = category.id
            break
        return category_id

    def add(self):
        name = get_text_input("Name")
        brewery_id = self._get_brewery_id()
        category_id = self._get_category_id()
        abv = None

        while abv is None:
            choice = input("ABV: ")
            try:
                choice = float(choice)
            except ValueError:
                print("Invalid choice")
                choice = None
                continue
            abv = choice

        beer = Beer(-1, brewery_id, name, category_id, abv)
        self.repository.insert(beer)

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
            if id is not None and self.repository.find_by_id(id) is None:
                id = None
                print("Not found")
        self.repository.delete(id)

    def list(self):
        beers = self.repository.find_all()
        print("Beers")
        print("----------")
        for beer in beers:
            print(f"{beer.id}. {beer.name}")

    def list_by_brewery(self):
        breweries = self.database.brewery.find_all()
        for i in range(len(breweries)):
            brewery = breweries[i]
            brewery_name = brewery.name
            print(f"{i}. {brewery_name}")

        brewery_id = None
        while True:
            choice = input("Brewery: ")
            try:
                choice = int(choice)
            except ValueError:
                choice = None
                print("Invalid choice")
                continue
            if choice < 0 or choice >= len(breweries):
                print("Invalid choice")
                continue
            brewery = breweries[choice]
            brewery_id = brewery.id
            break

        beers = self.repository.find_beers_by_brewer_id(brewery_id)
        print("Beers")
        print("----------")
        for beer in beers:
            print(f"{beer.id}. {beer.name}")
