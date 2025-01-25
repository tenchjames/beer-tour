from beer_repository import BeerRepository
from brewery_repository import BreweryRepository
from category_repository import CategoryRepository
from person_repository import PersonRepository
from tasting_attendee_repository import TastingAttendeeRepository


class Database():
    def __init__(self):
        self.brewery = BreweryRepository("db/brewery.csv")
        self.category = CategoryRepository("db/category.csv")
        self.beer = BeerRepository(
            "db/beers.csv",
            self.category.entities_by_id,
            self.brewery.entities_by_id)
        self.person = PersonRepository("db/person.csv")
        self.tasting_attendee = TastingAttendeeRepository(
            "db/tasting_attendee")

    def save(self):
        """
        self.brewery.save()
        self.category.save()
        self.beer.save()
        self.person.save()
        self.tasting_location.save()
        self.tasting_attendee.save()
        """
        pass
