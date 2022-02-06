import json

STRUKTUCRE = {"initialization":
                  {"file_password": "1234"},
              "Amazon": {"login": "Michael11Pl",
                         "password": "1234"}}


class File:

    def __init__(self):
        self.default_password_file_location = "data.json"
        self.actual_file_password = ""
        self.all_passwords = {}

    def load_file(self, file_location):
        def data_loader(data):
            self.actual_file_password = data["initialization"]["file_password"]
            data_keys = list(loaded_data.keys())
            for key in data_keys[1::]:
                self.all_passwords[key] = loaded_data[key]

        try:
            with open(file_location, "r") as file_load:
                loaded_data = json.load(file_load)
                data_loader(loaded_data)
        except FileNotFoundError or AttributeError:
            with open("data.json", "r") as file_load:
                loaded_data = json.load(file_load)
                data_loader(loaded_data)

    def save_file(self):
        with open("data.json", "w") as file_save:
            loaded_data = json.load(file_save)
            new_data = {"initialization": {"file_password": self.actual_file_password}}
            for key in list(self.all_passwords.keys()):
                new_data[key] = self.all_passwords[key]

            loaded_data.update(new_data)
            json.dump(new_data, file_save, indent=4)
