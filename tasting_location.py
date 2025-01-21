from util import slugify


class TastingLocation():
    def __init__(self, id, slug):
        self.id = id
        self.slug = slugify(slug)

    def clone(self):
        return TastingLocation(self.id, self.slug)

    def to_csv(self):
        return f"{self.id},{self.slug}"
