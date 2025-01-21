from util import is_valid_date


class Person():
    def __init__(self, id, lastname, firstname, birthdate):
        self.id = id
        if lastname is None or firstname is None or birthdate is None:
            raise ValueError("All fields are required")

        # if trimmed lastname, firstname, or birthdate is empty, raise error
        if lastname.strip() == "" or firstname.strip() == "" or birthdate.strip() == "":
            raise ValueError("All fields are required")

        if not is_valid_date(birthdate):
            raise ValueError("Invalid birthdate format. Use YYYY-MM-DD")

        self.lastname = lastname
        self.firstname = firstname
        self.birthdate = birthdate

    def clone(self):
        return Person(self.id, self.lastname, self.firstname, self.birthdate)

    def to_csv(self):
        # commas in names is silly, remove them
        lastname = self.lastname.replace(",", "")
        firstname = self.firstname.replace(",", "")
        return f"{self.id},{lastname},{firstname},{self.birthdate}"

    def __eq__(self, other):
        # we will make people equal if they have the same name and birthdate
        # (could two jane does be born on the same day...yea but for this app keep it simple)
        lower_firstname = self.firstname.lower() == other.firstname.lower()
        lower_lastname = self.lastname.lower() == other.lastname.lower()
        return lower_firstname and lower_lastname and self.birthdate == other.birthdate

    def __repr__(self):
        return f"Person({self.id}, {self.lastname}, {self.firstname}, {self.birthdate})"
