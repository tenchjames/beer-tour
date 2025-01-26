from util import get_numeric_input, get_text_input, is_valid_date
from person import Person
from page import Page


class PersonPage(Page):
    def __init__(self, database, router):
        self.database = database
        self.router = router

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
        print()
        print("Person Menu")
        print("0. Back")
        print("1. List")
        print("2. Create")
        print("3. Delete")
        print()
        choice = get_numeric_input("Choice")
        return choice

    def add(self):
        last_name = get_text_input("Last Name")
        first_name = get_text_input("First Name")
        is_valid_birthdate = False
        while not is_valid_birthdate:
            birth_date = get_text_input("Birth Date (yyyy-mm-dd) format")
            is_valid_birthdate = is_valid_date(birth_date)

        person = Person(-1, last_name, first_name, birth_date)
        self.database.person.insert(person)

    def delete(self):
        id = None
        print("Enter -1 to cancel")
        while id is None:
            id = get_numeric_input("Id: ")
            if id == -1:
                return
            if id is not None and self.database.person.find_by_id(id) is None:
                id = None
                print("Not found")
        self.repository.delete(id)

    def list(self):
        people = self.database.person.find_all()
        print("People")
        print("----------")
        for person in people:
            print(f"{person.id}. {person.lastname}, {
                  person.firstname} {person.birthdate}")
