import os


def main():
    if not os.path.exists("db/beers.csv"):
        with open("db/beers.csv", "w") as f:
            pass  # create the file if it does not exist
        with open("db/categories.csv", "w") as f:
            pass  # create the file if it does not exist
        with open("db/people.csv", "w") as f:
            pass  # create the file if it does not exist
        with open("db/beers-drank.csv", "w") as f:
            pass  # create the file if it does not exist
        with open("db/beers-drank-with.csv", "w") as f:
            pass  # create the file if it does not exist
        with open("db/brewery.csv", "w") as f:
            pass  # create the file if it does not exist

    print("Hello, World!")


if __name__ == "__main__":
    main()
