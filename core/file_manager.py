import json


class File:

    def __init__(self):
        self.default_password_file_location = "data.json"
        self.all_loaded_data = None
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
                self.all_loaded_data = loaded_data
        except FileNotFoundError or AttributeError:
            with open("data.json", "r") as file_load:
                loaded_data = json.load(file_load)
                data_loader(loaded_data)

    def save_file(self):
        with open("data.json", "w") as file_save:
            new_data = {"initialization": {"file_password": self.actual_file_password}}
            for key in list(self.all_passwords.keys()):
                new_data[key] = self.all_passwords[key]

            self.all_loaded_data.update(new_data)
            json.dump(new_data, file_save, indent=4)

    def create_new_file(self, file_path):
        try:
            with open(file_path, "w") as file:
                new_data = {"initialization": {"file_password": self.actual_file_password}}
                json.dump(new_data, file, indent=4)
        except AttributeError:
            with open("data.json", "w") as file:
                new_data = {"initialization": {"file_password": self.actual_file_password}}
                json.dump(new_data, file, indent=4)


#TODO 1: eliminate bug, when open file read file_path as Attribute Error and create new .json file
#TODO 2: eliminate bug when password is not added to File() class
#TODO 3: add AES