import boto3

def upload_to_s3():
    s3 = boto3.client('s3')
    bucket_name = 'sugnyani-patil'
    object_key = 'Config/config.yaml'
    file_path = 'config.yaml'

    print(f"Uploading {file_path} to s3://{bucket_name}/{object_key}...")
    s3.upload_file(file_path, bucket_name, object_key)
    print("Upload complete.")

if __name__ == "__main__":
    print("Hello, Hello, Hello world from GitHub Actions!")
    upload_to_s3()

