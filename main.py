from database import Database
from router import Router
from main_page import MainPage
from category_page import CategoryPage
from pages import Pages
from category import Category


def main():
    database = Database()

    router = Router()
    main = MainPage(database, router)
    cagegory = CategoryPage(database, router)
    router.add_route(Pages.MAIN, main)
    router.add_route(Pages.CATEGORY, cagegory)

    router.navigate(Pages.MAIN)

    while router.stack:
        router.execute()


if __name__ == "__main__":
    main()
