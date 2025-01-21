
class TastingAttendee():
    def __init__(self, id, tasting_id, person_id):
        self.id = id
        if tasting_id is None:
            raise ValueError("Tasting id is required")
        self.tasting_id = tasting_id
        if person_id is None:
            raise ValueError("Person/Attendee id is required")
        self.person_id = person_id

    def clone(self):
        return TastingAttendee(self.id, self.tasting_id, self.person_id)

    def to_csv(self):
        return f"{self.id},{self.tasting_id},{self.person_id}"
