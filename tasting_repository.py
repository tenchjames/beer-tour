from repository import Repository
from tasting import Tasting

fields = [
    "person_id",
    "beer_id",
    "tasting_date",
    "location_id",
    "cost",
    "paid_by_person_id",
    "rating"
]


class TastingRepository(Repository):
    def __init__(self, file_path):
        super().__init__(file_path, "tasting", fields, reader, writer)
        self.load()


def reader(line):
    id, person_id, beer_id, tasting_date, cost, paid_by_person_id, rating = line.strip().split(",")
    return Tasting(int(id), int(person_id), int(beer_id), tasting_date, cost, int(paid_by_person_id), rating)


def writer(entity):
    return entity.to_csv()
