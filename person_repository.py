from person import Person
from repository import Repository
from trie import Trie


class PersonRepository(Repository):
    def __init__(self, file_path):
        super().__init__(file_path, "person", [
            "lastname", "firstname", "birthdate"], reader, writer)
        self.load()

    def after_load(self):
        self.trie = Trie()
        for person in self.entities:
            last_name = person.lastname.lower()
            first_name = person.firstname.lower()
            name = f"{last_name}, {first_name}"
            first_name_first = f"{first_name} {last_name}"
            self.trie.insert(name, person)
            self.trie.insert(first_name_first, person)

    def insert(self, entity):
        super().insert(entity)
        last_name = entity.lastname.lower()
        first_name = entity.firstname.lower()
        name = f"{last_name}, {first_name}"
        first_name_first = f"{first_name} {last_name}"
        self.trie.insert(name, entity)
        self.trie.insert(first_name_first, entity)

    def search(self, query):
        query = query.lower()
        # todo: prevent duplicates in the trie in the first place
        results = self.trie.search(query)
        distinct_results = []
        seen = set()
        for result in results:
            if result.id not in seen:
                distinct_results.append(result)
                seen.add(result.id)

        return distinct_results


def reader(row):
    id = row[0]
    lastname = row[1]
    firstname = row[2]
    birthdate = row[3]
    return Person(int(id), lastname, firstname, birthdate)


def writer(entity):
    return [entity.id, entity.lastname, entity.firstname, entity.birthdate]
