from beer_repository import BeerRepository
from brewery_repository import BreweryRepository
from category_repository import CategoryRepository
from person_repository import PersonRepository
from tasting_attendee_repository import TastingAttendeeRepository
from tasting_repository import TastingRepository


class Database():
    def __init__(self):
        self.brewery = BreweryRepository("db/brewery.csv")
        self.category = CategoryRepository("db/category.csv")
        self.beer = BeerRepository(
            "db/beers.csv",
            self.category.entities_by_id,
            self.brewery.entities_by_id)
        self.person = PersonRepository("db/person.csv")
        self.tasting = TastingRepository("db/tasting.csv")
        self.tasting_attendee = TastingAttendeeRepository(
            "db/tasting_attendee")
