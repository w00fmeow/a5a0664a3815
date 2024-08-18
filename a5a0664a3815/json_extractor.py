import json
from .file_extractor import FileExtractor


class JSONExtractor(FileExtractor):
    def __init__(self, credentials_json_key="credentials"):
        super().__init__([".json"])

        self.credentials_json_key = credentials_json_key

    def process_file(self, file_path):
        with open(file_path, mode="r") as file:
            data = json.load(file)

            for object in data[self.credentials_json_key]:
                self.extract_credentials_from_object(object, file_path)

    def extract_credentials_from_object(self, object, file_path):
        try:
            password = object["password"]
            email = object["email"]

            super().add_credentials(email, password, file_path)
        except Exception as e:
            pass
