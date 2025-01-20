

class Category():
    def __init__(self, id, name, description=''):
        self.id = id
        if name is None or name.strip() == "":
            raise ValueError("Name is required")
        self.name = name
        self.description = description

    def clone(self):
        return Category(self.id, self.name, self.description)

    def to_csv(self):
        name = self.name
        if ',' in name:
            name = f'"{name}"'
        description = self.description
        if self.description is None:
            description = ''
        if ',' in description:
            description = f'"{description}"'
        return f"{self.id},{name},{description}"
