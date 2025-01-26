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


def standard_admin_menu(name):
    print()
    print(f"{name} Menu")
    print("0. Back")
    print("1. List")
    print("2. Create")
    print("3. Delete")
    print()
    choice = None
    while choice is None:
        choice = input("Choice: ")
        try:
            choice = int(choice)
        except ValueError:
            choice = None
            print("Invalid choice")
    return choice


def get_text_input(field_name):
    field = None
    while field is None:
        field = input(f"{field_name}: ")
        if field == "":
            print(f"{field_name} cannot be empty")
            field = None
    return field


def get_numeric_input(field_name):
    field = None
    while field is None:
        field = input(f"{field_name}: ")
        if field == "":
            print(f"{field_name} cannot be empty")
            field = None
        try:
            field = int(field)
        except ValueError:
            print(f"{field_name} must be a number")
            field = None
    return field
