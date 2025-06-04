import boto3

s3 = boto3.client ('s3')

response = s3.list_buckets()
buckets = response['Buckets']

for bucket in buckets:
    bucket_name = bucket['Name']

try:
    encryption = s3.get_bucket_encryption(Bucket=bucket_name)
    print(f"Bucket : {bucket_name} - Encryption Enabled")
except s3.exceptions.ClientError as e:
    error_code = e.response ['Error']['Code']
    if error_code == 'ServerSideEncryptionConfigurationNotFoundError':
        print(f"Bucket : {bucket_name} - Encryption not Enabled")
    else:
         print(f"Bucket : {bucket_name} - Error is : {error_code}")   
