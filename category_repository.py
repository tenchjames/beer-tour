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


def reader(line):
    id, name, description = line.strip().split(",")
    return Category(int(id), name, description)


def writer(entity):
    return entity.to_csv()
