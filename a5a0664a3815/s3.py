import boto3, os

class S3Service:
    def __init__(self, s3_bucket_name, s3_access_key, s3_secret):
        self.s3_bucket_name = s3_bucket_name


        self.s3 = boto3.client('s3',
                  aws_access_key_id=s3_access_key,
                  aws_secret_access_key=s3_secret)
        
    def get_all_file_keys(self):
        object_keys = []
        response = self.s3.list_objects_v2(Bucket=self.s3_bucket_name)

        if 'Contents' in response:
            for obj in response['Contents']:
                object_keys.append(obj['Key'])

        return object_keys
    
    def download_bucket_content(self, output_dir):

        file_keys = self.get_all_file_keys()
        if not file_keys:
            print("S3 bucket is empty. Skipping..")
        else:
            print("Starting to download {len(file_keys)} files")

        downloaded_files = []

        for key in file_keys:
            output_path = os.path.join(output_dir, key)
            
            print(f"Downloading: {key} to {output_path}. Please, wait...")

            
            self.s3.download_file(self.s3_bucket_name, key, output_path)
            
            print(f"Downloaded: {output_path}")

            downloaded_files.append(output_path)

        return downloaded_files

    