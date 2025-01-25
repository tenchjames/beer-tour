from brewery import Brewery
from repository import Repository


class BreweryRepository(Repository):
    def __init__(self, file_path):
        super().__init__(file_path, "brewery", [
            "name", "city", "state"], reader, writer)
        super().load()


def reader(row):
    id = row[0]
    name = row[1]
    city = row[2]
    state = row[3]
    country = row[4]
    return Brewery(int(id), name, city, state, country)


def writer(entity):
    return [entity.id, entity.name, entity.city, entity.state, entity.country]
