import os.path
import json


class JsonHelper:

    def __init__(self, data_directory):

        self.data_directory = data_directory

    def get_data(self):
        if os.path.exists(self.data_directory):
            with open(self.data_directory, "r") as file:
                data = json.load(file)
                return data
        return None

    def add_in_data(self, data):
        self.data_directory_exists()
        if os.path.exists(self.data_directory):

            with open(self.data_directory, "r") as file:
                existing_data = json.load(file)

            existing_data.append(data)

            with open(self.data_directory, "w") as file:
                json.dump(existing_data, file, indent=4)

        else:
            with open(self.data_directory, "w") as file:
                json.dump([data], file, indent=4)

    def delete_tournament(self, tournament_to_delete):

        with open(self.data_directory, "r") as file:
            existing_data = json.load(file)

        new_data = []

        for tournament in existing_data:
            if tournament["Name"].lower() != tournament_to_delete.name.lower():
                new_data.append(tournament)

        with open(self.data_directory, "w") as file:
            json.dump(new_data, file, indent=4)

    def data_directory_exists(self):
        data_directory = (self.data_directory[:self.data_directory.rfind("/")])
        if not os.path.exists(data_directory):
            os.mkdir(data_directory)
