from repository import Repository
from tasting_attendee import TastingAttendee

fields = ["tasting_id", "person_id"]


class TastingAttendeeRepository(Repository):
    def __init__(self, file_path):
        super().__init__(file_path, "tasting_attendee", fields, reader, writer)
        self.load()


def reader(line):
    id, tasting_id, person_id = line.strip().split(",")
    return TastingAttendee(int(id), int(tasting_id), int(person_id))


def writer(entity):
    return entity.to_csv()
