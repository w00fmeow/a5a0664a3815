import csv
from .file_extractor import FileExtractor


class CSVExtractor(FileExtractor):
    def __init__(self, has_header_row=True):
        self.has_header_row = has_header_row
        super().__init__([".csv", ".CSV"])

    def process_file(self, file_path):
        with open(file_path, mode="r") as file:
            csv_reader = csv.reader(file)
            password_column_index = 0
            email_column_index = 1

            if self.has_header_row:
                headers = next(csv_reader)

                password_column_index = headers.index("password")
                email_column_index = headers.index("email")

            for row in csv_reader:
                self.extract_credentials_from_row(
                    row, password_column_index, email_column_index, file_path
                )

    def extract_credentials_from_row(
        self, row, password_column_index, email_column_index, file_path
    ):
        try:
            password = row[password_column_index]
            email = row[email_column_index]

            super().add_credentials(email, password, file_path)
        except Exception as e:
            pass
