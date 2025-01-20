
class Person():
    def __init__(self, id, name, birthdate):
        self.id = id
        self.name = name
        self.birthdate = birthdate

    def to_csv(self):
        name = self.name
        if ',' in name:
            name = f'"{name}"'
        return f"{self.id},{name},{self.birthdate}"
