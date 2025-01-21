from repository import Repository
from tasting_location import TastingLocation

fields = ["slug"]


class TastingLocationRepository(Repository):
    def __init__(self, file_path):
        super().__init__(file_path, "tasting_location", fields, reader, writer)
        self.load()


def reader(line):
    id, slug = line.strip().split(",")
    return TastingLocation(int(id), slug)


def writer(entity):
    entity.to_csv()
