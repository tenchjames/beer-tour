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


def reader(line):
    id, brewery_id, name, category_id, abv = line.strip().split(",")
    return Beer(int(id), int(brewery_id), name, int(category_id), abv)


def writer(entity):
    return entity.to_csv()
