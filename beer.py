
class Beer():
    def __init__(self, id, brewery, name, category, abv):
        self.id = id
        if brewery is None:
            raise ValueError("Brewery is required")
        self.brewery = brewery
        if name is None or name.strip() == "":
            raise ValueError("Name is required")
        self.name = name
        if category is None:
            raise ValueError("Category is required")
        self.category = category
        self.abv = abv

    def to_csv(self):
        brewery = self.brewery
        brewery_id = brewery.id
        name = self.name
        if ',' in name:
            name = f'"{name}"'
        category = self.category
        category_id = category.id
        abv = self.abv
        if abv is None:
            abv = 0.0
        return f"{self.id},{brewery_id},{name},{category_id},{abv}"
