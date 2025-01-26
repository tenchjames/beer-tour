
from tasting import Tasting
from page import Page
from util import get_text_input, get_numeric_input, is_valid_date


class TastingPage(Page):
    def __init__(self, database, router):
        self.database = database
        self.router = router
        self.state = {}

    def execute(self):
        while True:
            choice = self.prompt()
            if choice == 0:
                break
            match choice:
                case 1:
                    self.summary()
                case 2:
                    self.add()
                case 3:
                    self.delete()
                case _:
                    print("Invalid choice")
                    self.prompt()
        self.router.back()

    def prompt(self):
        print()
        print("Record a Drink Menu")
        print("0. Back")
        print("1. Summary")
        print("2. Add a drink")
        print("3. Delete a drink")
        print("More statics and random beer picker coming soon...")
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

    def _get_person(self):
        selected_person = None
        isSelecting = True
        while selected_person is None and isSelecting:
            while isSelecting:
                name = get_text_input("Name")
                possible = self.database.person.search(name)
                for i in range(len(possible)):
                    person = possible[i]
                    print(f"{i}. {person.lastname}, {person.firstname}")
                print("Enter -1 to cancel")
                person_index = None
                while person_index is None:
                    person_index = get_numeric_input("Person ID")
                if person_index == -1:
                    search_again = get_text_input("Search again? (y/n)")
                    if search_again == "n":
                        isSelecting = False
                elif person_index < -1 or person_index >= len(possible):
                    print("Invalid choice")
                else:
                    selected_person = possible[person_index]
                    isSelecting = False
        return selected_person

    def _get_beer(self):
        is_valid = False
        while not is_valid:
            breweries = self.database.brewery.find_all()
            for brewery in breweries:
                print(f"{brewery.id}. {brewery.name}")

            brewery_id = None
            while brewery_id is None:
                brewery_id = get_numeric_input("Pick a brewery (enter id)")

            beers = self.database.beer.find_beers_by_brewer_id(brewery_id)
            if len(beers) == 0:
                print("No beers found for that brewery")
                continue
            for beer in beers:
                print(f"{beer.id}. {beer.name}")

            beer_id = None
            while beer_id is None:
                beer_id = get_numeric_input("Pick a beer (enter id)")

            beer = self.database.beer.find_by_id(beer_id)
            if beer is None:
                print("Invalid beer id")
            else:
                return beer

    def add(self):
        # who drank the beer, what beer, what date, how much did the beer cost in dollars, who paid, rating
        print("Who drank the beer?")
        person = self._get_person()

        beer = self._get_beer()
        tasting_date_is_valid = False
        while not tasting_date_is_valid:
            tasting_date = get_text_input("Tasting Date (yyyy-mm-dd) format")
            tasting_date_is_valid = is_valid_date(tasting_date)

        cost = get_numeric_input("Cost in dollars")

        print("Who paid?")
        paid_by = self._get_person()

        is_valid_rating = False
        while not is_valid_rating:
            rating = get_numeric_input("Rating (0 to 5)")
            if rating < 0 or rating > 5:
                print("Rating must be between 0 and 5")
            else:
                is_valid_rating = True

        tasting = Tasting(-1, person.id, beer.id, tasting_date,
                          cost, paid_by.id, rating)
        self.database.tasting.insert(tasting)

    def delete(self):
        id = None
        print("Enter -1 to cancel")
        while id is None:
            id = get_numeric_input("Id: ")
            if id == -1:
                return
        self.repository.delete(id)

    def summary(self):
        pass
