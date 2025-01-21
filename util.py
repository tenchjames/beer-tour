import re

date_pattern = re.compile(
    r"^(19|20)\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$")


def is_valid_date(date_to_test):
    return re.match(date_pattern, date_to_test) is not None


def slugify(slug):
    slug = slug.lower()
    slug = re.sub(r"[^\w\s]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    slug = re.sub(r"^\s+|\s+$", "", slug)
    slug = re.sub(r"-+", "-", slug)
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug
