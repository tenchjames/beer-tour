from page import Page
from brewery import Brewery
from util import standard_admin_menu


class BreweryPage(Page):
    def __init__(self, countries, database, router):
        self.countries = countries
        self.database = database
        self.repository = database.brewery
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
        return standard_admin_menu("Brewery")

    def add(self):
        name = None
        city = None
        state = None
        country = None
        while name is None:
            name = input("Name: ")
            if name == "":
                print("Name cannot be empty")
                name = None

        while country is None:
            choice = 0
            countries_per_page = 10
            index = 0
            while (choice < 1 or choice > len(self.countries)) and index < len(self.countries):
                while index < len(self.countries):
                    for i in range(index, index + countries_per_page):
                        if i < len(self.countries):
                            print(f"{i + 1}. {self.countries[i]["name"]}")
                    next_index = i + 1
                    if next_index < len(self.countries):
                        print("0. Next Page")
                    choice = input("Country: ")
                    try:
                        choice = int(choice)
                    except ValueError:
                        print("Invalid choice")

                    index = next_index

                    if choice == 0 and next_index < len(self.countries):
                        continue

                    if choice > -1 and choice <= len(self.countries):
                        country = self.countries[choice - 1]
                        break
                if choice > -1 and choice <= len(self.countries):
                    country = self.countries[choice - 1]
                    break
                else:
                    print("Invalid choice")
                    choice = input("Country: ")
                    try:
                        choice = int(choice)
                    except ValueError:
                        pass

        while state is None:
            state = input("State: ")

        while city is None:
            city = input("City: ")
            if city == "":
                print("City cannot be empty")
                city = None

        brewery = Brewery(-1, name, city, state, country["name"])

        self.repository.insert(brewery)

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
        breweries = self.repository.find_all()
        print("Breweries")
        print("----------")
        for brewery in breweries:
            print(f"{brewery.id}. {brewery.name}")
