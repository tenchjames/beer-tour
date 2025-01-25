import csv
import os
import requests
from constants import WORLD_BANK_COUNTRY_API_JSON_URL


class CountryClient():
    def __init__(self):
        self.countries = []
        self.file_path = 'db/countries.csv'
        self.next_id = 1
        self.load()

    def load(self):
        if not os.path.exists(self.file_path):
            response = requests.get(WORLD_BANK_COUNTRY_API_JSON_URL)
            if response.status_code != 200:
                return
            data = response.json()
            meta = data[0]
            countries = data[1]
            for country in countries:
                if country["region"]["value"] == "Aggregates":
                    continue
                if country["name"] is None or country["name"].strip() == "":
                    continue
                self.countries.append(
                    {"id": self.next_id, "name": country["name"]})
                self.next_id += 1

            page = meta["page"]
            pages = meta["pages"]
            while page < pages:
                url = f"{WORLD_BANK_COUNTRY_API_JSON_URL}&page={page+1}"
                response = requests.get(url)
                if response.status_code != 200:
                    return
                data = response.json()
                meta = data[0]
                countries = data[1]
                for country in countries:
                    if country["region"]["value"] == "Aggregates":
                        continue
                    if country["name"] is None or country["name"].strip() == "":
                        continue
                    self.countries.append(
                        {"id": self.next_id, "name": country["name"]})
                    self.next_id += 1
                page = meta["page"]

            usa_index = -1
            for i in range(len(self.countries)):
                if self.countries[i]["name"] == "United States":
                    usa_index = i
                    break
            if usa_index > -1:
                usa = self.countries.pop(usa_index)
                self.countries.insert(0, usa)

            with open(self.file_path, "w") as f:
                writer = csv.writer(f, quotechar='"', delimiter=",")
                for country in self.countries:
                    name = country['name']
                    if ',' in name:
                        name = f'"{name}"'
                    writer.writerow([country["id"], name])

        else:
            with open(self.file_path, "r") as f:
                reader = csv.reader(f, quotechar='"', delimiter=",")
                for row in reader:
                    id, name = row
                    self.countries.append({"id": int(id), "name": name})
