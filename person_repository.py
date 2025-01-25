from person import Person
from repository import Repository


class PersonRepository(Repository):
    def __init__(self, file_path):
        super().__init__(file_path, "person", [
            "lastname", "firstname", "birthdate"], reader, writer)
        self.load()


def reader(row):
    id = row[0]
    lastname = row[1]
    firstname = row[2]
    birthdate = row[3]
    return Person(int(id), lastname, firstname, birthdate)


def writer(entity):
    return [entity.id, entity.lastname, entity.firstname, entity.birthdate]
