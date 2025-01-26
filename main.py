from database import Database
from router import Router
from main_page import MainPage
from category_page import CategoryPage
from brewery_page import BreweryPage
from pages import Pages
from country_client import CountryClient
from beer_page import BeerPage
from tasting_page import TastingPage
from person_page import PersonPage


def main():
    database = Database()

    country_client = CountryClient()
    router = Router()
    main = MainPage(database, router)
    cagegory = CategoryPage(database, router)
    brewery = BreweryPage(country_client.countries, database, router)
    beer = BeerPage(database, router)
    tasting = TastingPage(database, router)
    person = PersonPage(database, router)

    router.add_route(Pages.MAIN, main)
    router.add_route(Pages.CATEGORY, cagegory)
    router.add_route(Pages.BREWERY, brewery)
    router.add_route(Pages.BEERS, beer)
    router.add_route(Pages.TASTINGS, tasting)
    router.add_route(Pages.PERSON, person)

    router.navigate(Pages.MAIN)

    while router.stack:
        router.execute()


if __name__ == "__main__":
    main()
