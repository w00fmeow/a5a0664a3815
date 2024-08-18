import json, re
from .file_extractor import FileExtractor

pattern = r"\('([^']*)',[^']*,'([^']*)'"


class SQLExtractor(FileExtractor):
    def __init__(self):
        super().__init__([".sql", ".SQL"])

    def process_file(self, file_path):
        with open(file_path, mode="r") as file:
            sql_content = file.read()

            matches = re.findall(pattern, sql_content)

            for email, password in matches:
                self.add_credentials(email, password, file_path)

    def extract_credentials_from_object(self, email, password, file_path):
        try:
            super().add_credentials(email, password, file_path)
        except Exception as e:
            pass
