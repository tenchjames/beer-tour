from util import is_valid_date


class Tasting():
    def __init__(self, id, person_id, beer_id, location_id, tasting_date, cost, paid_by_person_id, rating):
        self.id = id
        if person_id is None:
            raise ValueError("Person id is required")
        self.person_id = person_id
        if beer_id is None:
            raise ValueError("Beer id is required")
        self.beer_id = beer_id
        if tasting_date is None:
            raise ValueError("Tasting date is required")
        if not is_valid_date(tasting_date):
            raise ValueError("Invalid tasting date format. Use YYYY-MM-DD")
        self.tasting_date = tasting_date
        # store cost in dollars
        if cost is None:
            raise ValueError("Cost is required")
        if type(cost) is not int or cost < 0:
            raise ValueError("Cost must be a positive integer")
        self.cost = cost
        if paid_by_person_id is None:
            raise ValueError("Paid by person id is required")
        self.paid_by_person_id = paid_by_person_id
        if rating is None:
            raise ValueError("Rating is required")
        if type(rating) is not int or rating < 0 or rating > 5:
            raise ValueError("Rating must be an integer between 0 and 5")
        self.rating = rating

    def clone(self):
        return Tasting(self.id, self.person_id, self.beer_id, self.location_id, self.tasting_date, self.cost, self.paid_by_person_id, self.rating)

    def to_csv(self):
        return f"{self.id},{self.person_id},{self.beer_id},{self.location_id},{self.tasting_date},{self.cost},{self.paid_by_person_id},{self.rating}"
