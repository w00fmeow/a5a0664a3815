import click
from .s3 import S3Service
from .json_extractor import JSONExtractor
from .csv_extractor import CSVExtractor
from .file_extractor import output_all_credentials
from .sql_extractor import SQLExtractor


@click.command()
@click.option("--s3_bucket_name", help="S3 bucket name", required=True)
@click.option("--s3_access_key", help="S3 access key", required=True)
@click.option("--s3_secret", help="S3 secret", required=True)
def run(s3_bucket_name, s3_access_key, s3_secret):
    s3_service = S3Service(s3_bucket_name, s3_access_key, s3_secret)

    downloaded_files = s3_service.download_bucket_content(output_dir="/tmp")

    extractors = [
        SQLExtractor(),
        CSVExtractor(has_header_row=True),
        JSONExtractor(credentials_json_key="credentials"),
    ]

    for file_path in downloaded_files:
        for extractor in extractors:

            if extractor.is_file_path_supported(file_path):
                extractor.add_file(file_path)
                break

    files_count = sum([len(extractor.get_all_files()) for extractor in extractors])

    print(f"Starting to process {files_count} files")

    for extractor in extractors:
        extractor.process_all_files()

    output_all_credentials(extractors)
