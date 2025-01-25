from category import Category
from repository import Repository

fields = [
    ("name", "string"),
    ("description", "string")
]


class CategoryRepository(Repository):
    def __init__(self, file_path):
        super().__init__(file_path, "category", fields, reader, writer)
        self.load()


def reader(row):
    id = row[0]
    name = row[1]
    description = row[2]
    return Category(int(id), name, description)


def writer(entity):
    return [entity.id, entity.name, entity.description]
