from beer import Beer
from repository import Repository


class BeerRepository(Repository):
    def __init__(self, file_path, categories_by_id, breweries_by_id):
        super().__init__(file_path, "beer", [
            "brewery_id", "name", "category_id", "abv"], reader, writer)
        self.categories_by_id = categories_by_id
        self.breweries_by_id = breweries_by_id
        self.by_brewery_id = {}
        self.by_category_id = {}
        self.load()

    def after_load(self):
        for entity in self.entities:
            if self.by_brewery_id.get(entity.brewery.id) is None:
                self.by_brewery_id[entity.brewery.id] = []
            self.by_brewery_id[entity.brewery.id].append(entity)
            if self.by_category_id.get(entity.category.id) is None:
                self.by_category_id[entity.category.id] = []
            self.by_category_id[entity.category.id].append(entity)

    def find_beers_by_brewer_id(self, brewery_id):
        if brewery_id is None:
            return []
        if brewery_id not in self.by_brewery_id:
            return []
        return self.by_brewery_id[brewery_id]

    def insert(self, entity):
        inserted = super().insert(entity)
        self.by_brewery_id[entity.brewery_id].append(
            self.entities_by_id[inserted.id])
        return inserted


def reader(row):
    id = row[0]
    brewery_id = row[1]
    name = row[2]
    category_id = row[3]
    abv = row[4]
    return Beer(int(id), int(brewery_id), name, int(category_id), abv)


def writer(entity):
    return [entity.id, entity.brewery_id, entity.name, entity.category_id, entity.abv]
