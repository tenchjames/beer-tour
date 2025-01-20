
class Beer():
    def __init__(self, id, brewery_id, name, category_id, abv):
        self.id = id
        if brewery_id is None:
            raise ValueError("Brewery id is required")
        self.brewery_id = brewery_id
        if name is None or name.strip() == "":
            raise ValueError("Name is required")
        self.name = name
        if category_id is None:
            raise ValueError("Category id is required")
        self.category_id = category_id
        self.abv = abv

    def clone(self):
        return Beer(self.id, self.brewery_id, self.name, self.category_id, self.abv)

    def to_csv(self):
        name = self.name
        if ',' in name:
            name = f'"{name}"'
        abv = self.abv
        if abv is None:
            abv = 0.0
        return f"{self.id},{self.brewery_id},{name},{self.category_id},{abv}"
