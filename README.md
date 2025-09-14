# AWS Cloud Security Automation
Python-based tools and scripts for automating security tasks on AWS (IAM, EC2, S3), including:
- IAM user and role management (`iam_boto3.py`, `iamrole_tf.py`)
- EC2 automated provisioning with custom IAM roles (`ec2_iam_project.py`)
- S3 security automation (`s3_enable.py`)
- [`iam_policy_audit.py`](AWS/iam_policy_audit.py) — Script to analyze AWS IAM policies for security risks (wildcards, overly broad access, best-practice violations). Usage: `python AWS/iam_policy_audit.py <policy_file.json>`
- Terraform config generation

## Features
- Automates key AWS security tasks for better consistency and speed
- Uses Boto3 for live AWS management and can output Terraform for reproducible IaC

## Folder Structure
