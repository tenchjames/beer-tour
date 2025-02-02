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

    def find_by_date(self, date):
        return [tasting for tasting in self.entities if tasting.tasting_date == date]


def reader(row):
    id = row[0]
    person_id = row[1]
    beer_id = row[2]
    tasting_date = row[3]
    cost = row[4]
    paid_by_person_id = row[5]
    rating = row[6]
    return Tasting(int(id), int(person_id), int(beer_id), tasting_date, cost, int(paid_by_person_id), rating)


def writer(entity):
    return [entity.id, entity.person_id, entity.beer_id, entity.tasting_date, entity.cost, entity.paid_by_person_id, entity.rating]
