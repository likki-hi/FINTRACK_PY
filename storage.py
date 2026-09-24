import json

FILE_NAME = "data.json"


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data(transactions):
    with open(FILE_NAME, "w") as file:
        json.dump(transactions, file, indent=4)

    print("✅ Data saved successfully!")