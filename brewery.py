

class Brewery():
    def __init__(self, id, name, city, state, country):
        self.id = id
        if name is None or name.strip() == "":
            raise ValueError("Name is required")
        self.name = name
        self.city = city
        self.state = state
        self.country = country

    def to_csv(self):
        name = self.name
        if ',' in name:
            name = f'"{name}"'
        city = self.city
        if ',' in self.city:
            city = f'"{self.city}"'
        state = self.state
        if ',' in self.state:
            state = f'"{self.state}"'
        country = self.country
        if ',' in self.country:
            country = f'"{self.country}"'
        return f"{self.id},{name},{city},{state},{country}"
