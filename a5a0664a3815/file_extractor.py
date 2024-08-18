import os, re, csv

email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"


class FileExtractor:

    def __init__(self, supported_file_extentions):
        self.file_to_credentials_map = {}
        self.supported_file_extentions = supported_file_extentions

    def get_supported_file_extentions(self):
        return self.supported_file_extentions

    def is_file_path_supported(self, file_path):
        _, file_extension = os.path.splitext(file_path)

        return file_extension in self.supported_file_extentions

    def add_file(self, file_path):
        self.file_to_credentials_map[file_path] = []

    def get_all_files(self):
        return self.file_to_credentials_map.keys()

    def process_all_files(self):
        for file_path in self.get_all_files():
            print(f"Processing file: {file_path}")
            self.process_file(file_path)

    def process_file(self, file_path):
        raise NotImplementedError("Subclasses should implement this method")

    def add_credentials(self, email, password, file_path):
        if not self.is_email_valid(email):
            return

        self.file_to_credentials_map[file_path].append([email, password])

    def is_email_valid(self, email):
        return re.match(email_pattern, email) is not None


def output_all_credentials(extractors):
    file_path = "output.csv"

    headers_row = ["file_name", "email", "password"]

    with open(file_path, mode="w", newline="") as file:
        csv_writer = csv.writer(file)
        data = [headers_row]

        for extractor in extractors:

            for file_path in extractor.get_all_files():
                file_name = os.path.basename(file_path)

                credentials = extractor.file_to_credentials_map[file_path]

                for [email, password] in credentials:
                    data.append([file_name, email, password])

        csv_writer.writerows(data)
