# cloud_setup.py

import boto3

def upload_to_s3(file_name, bucket, object_name=None):
    s3_client = boto3.client('s3')
    if object_name is None:
        object_name = file_name
    s3_client.upload_file(file_name, bucket, object_name)

def main():
    upload_to_s3('cleaned_weather_data.csv', 'my-s3-bucket')

if __name__ == "__main__":
    main()
