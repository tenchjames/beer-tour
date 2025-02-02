
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
                case 4:
                    self.list_by_date()
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
        print("4. List by date")
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
        self.database.tasting.delete(id)

    def summary(self):
        people = self.database.person.find_all()
        people_by_id = {}
        for person in people:
            people_by_id[person.id] = person

        tastings = self.database.tasting.find_all()
        tastings_by_person = {}
        paid_tastings_by_person = {}
        for person in people:
            tastings_by_person[person.id] = []
            paid_tastings_by_person[person.id] = []

        for tasting in tastings:
            tastings_by_person[tasting.person_id].append(tasting)
            paid_tastings_by_person[tasting.paid_by_person_id].append(tasting)

        beer_summary_by_person = {}

        for person in people:
            beer_summary_by_person[person.id] = {}
            for tasting in tastings_by_person[person.id]:
                beer_id = tasting.beer_id
                if beer_id not in beer_summary_by_person[person.id]:
                    beer_summary_by_person[person.id][beer_id] = 0
                beer_summary_by_person[person.id][beer_id] += 1

        total_spent_per_person = {}
        for person in people:
            total_spent_per_person[person.id] = 0
            for tasting in paid_tastings_by_person[person.id]:
                total_spent_per_person[person.id] += tasting.cost

        print("Summary")
        for person_id in beer_summary_by_person:
            person = people_by_id[person_id]
            print(f"{person.lastname}, {person.firstname}")
            for beer_id in beer_summary_by_person[person_id]:
                beer = self.database.beer.find_by_id(beer_id)
                count = beer_summary_by_person[person_id][beer_id]
                print(f"  {beer.name}: {count}")
            print(f"Total spent: ${total_spent_per_person[person_id]}")

    def list_by_date(self):
        date = get_text_input("Date (yyyy-mm-dd) format")
        tastings = self.database.tasting.find_by_date(date)
        for tasting in tastings:
            person = self.database.person.find_by_id(tasting.person_id)
            beer = self.database.beer.find_by_id(tasting.beer_id)
            paid_by = self.database.person.find_by_id(
                tasting.paid_by_person_id)
            print(f"{tasting.id}. {person.lastname}, {person.firstname} drank {beer.name} on {tasting.tasting_date} for ${
                  tasting.cost} paid by {paid_by.lastname}, {paid_by.firstname} with a rating of {tasting.rating}")
