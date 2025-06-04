import boto3
import botocore.exceptions

# Take input from the user
username = input("Enter IAM username to create: ")
policy_arn = input("Enter IAM policy ARN to attach: ")

# Initialize IAM client
iam = boto3.client('iam')

try:
    response = iam.create_user(UserName=username)
    print(f"User{username} has been created")

except botocore.exceptions.ClientError as error:
    print(f"Failed to create user : {error.response['Error']['Message']}")

try:
    response = iam.attach_user_policy(
        UserName=username,
        PolicyArn=policy_arn    
    )
    print(f"user policy has been attached")
except botocore.exceptions.ClientError as error:
    print(f"failed to attach policy : {error.response['Error']['Message']}")