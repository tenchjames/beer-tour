from beer_repository import BeerRepository
from brewery_repository import BreweryRepository
from category_repository import CategoryRepository
from person_repository import PersonRepository
from person import Person


def main():
    brewery_repository = BreweryRepository("db/brewery.csv")
    category_repository = CategoryRepository("db/categories.csv")
    brewery_repository = BeerRepository(
        "db/beers.csv",
        category_repository.categories_by_id,
        brewery_repository.breweries_by_id)
    people_repository = PersonRepository("db/people.csv")

    james = Person(-1, "James", "T", "1975-10-25")
    jackie = Person(-1, "Jackie", "T", "1976-11-20")
    james = people_repository.insert(james)
    james = people_repository.insert(jackie)
    people = people_repository.find_all()
    for person in people:
        print(person)


if __name__ == "__main__":
    main()
