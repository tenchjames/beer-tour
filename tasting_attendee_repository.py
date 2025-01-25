from repository import Repository
from tasting_attendee import TastingAttendee

fields = ["tasting_id", "person_id"]


class TastingAttendeeRepository(Repository):
    def __init__(self, file_path):
        super().__init__(file_path, "tasting_attendee", fields, reader, writer)
        self.load()


def reader(row):
    id = row[0]
    tasting_id = row[1]
    person_id = row[2]
    return TastingAttendee(int(id), int(tasting_id), int(person_id))


def writer(entity):
    return [entity.id, entity.tasting_id, entity.person_id]
