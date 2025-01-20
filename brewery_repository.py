from brewery import Brewery
from repository import Repository


class BreweryRepository(Repository):
    def __init__(self, file_path):
        super().__init__(file_path, "brewery", [
            "name", "city", "state"], reader, writer)
        self.load()


def reader(line):
    id, name, city, state = line.strip().split(",")
    return Brewery(int(id), name, city, state)


def writer(entity):
    return entity.to_csv()
