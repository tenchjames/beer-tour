from util import is_valid_date


class Tasting():
    def __init__(self, id, person_id, beer_id, tasting_date, cost, paid_by_person_id, rating):
        self.id = id
        if person_id is None:
            raise ValueError("Person id is required")
        try:
            person_id = int(person_id)
        except ValueError:
            raise ValueError("Person id must be an integer")

        self.person_id = person_id
        if beer_id is None:
            raise ValueError("Beer id is required")
        try:
            beer_id = int(beer_id)
        except ValueError:
            raise ValueError("Beer id must be an integer")
        self.beer_id = beer_id
        if tasting_date is None:
            raise ValueError("Tasting date is required")
        if not is_valid_date(tasting_date):
            raise ValueError("Invalid tasting date format. Use YYYY-MM-DD")
        self.tasting_date = tasting_date
        # store cost in dollars
        if cost is None:
            raise ValueError("Cost is required")
        try:
            cost = int(cost)
        except ValueError:
            raise ValueError("Cost must be a positive integer")
        if cost < 0:
            raise ValueError("Cost must be a positive integer")
        self.cost = cost
        if paid_by_person_id is None:
            raise ValueError("Paid by person id is required")
        try:
            paid_by_person_id = int(paid_by_person_id)
        except ValueError:
            raise ValueError("Paid by person id must be an integer")
        self.paid_by_person_id = paid_by_person_id
        if rating is None:
            raise ValueError("Rating is required")
        try:
            rating = int(rating)
        except ValueError:
            raise ValueError("Rating must be an integer")
        if rating < 0 or rating > 5:
            raise ValueError("Rating must be an integer between 0 and 5")
        self.rating = rating

    def clone(self):
        return Tasting(self.id, self.person_id, self.beer_id, self.tasting_date, self.cost, self.paid_by_person_id, self.rating)
