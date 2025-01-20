from person import Person
from repository import Repository


class PersonRepository(Repository):
    def __init__(self, file_path):
        super().__init__(file_path, "person", [
            "lastname", "firstname", "birthdate"], reader, writer)
        self.load()


def reader(line):
    id, lastname, firstname, birthdate = line.strip().split(",")
    return Person(int(id), lastname, firstname, birthdate)


def writer(entity):
    entity.to_csv()
