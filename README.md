# Cloud Security Automation
Python-based tools and scripts for automating security tasks on AWS (IAM, EC2, S3), including:
- [`iam_boto3.py`](AWS/iam_boto3.py) — Script for automated IAM user management and policy operations using Boto3. Usage: `python AWS/iam_boto3.py`
- [`iamrole_tf.py`](AWS/iamrole_tf.py) — Script for IAM role creation and management with Terraform configuration generation. Usage: `python AWS/iamrole_tf.py`
- [`ec2_iam_project.py`](AWS/ec2_iam_project.py) — Script for automated EC2 instance provisioning with custom IAM roles and security configurations. Usage: `python AWS/ec2_iam_project.py`
- [`s3_enable.py`](AWS/s3_enable.py) — Script for S3 bucket security automation including encryption, versioning, and access control setup. Usage: `python AWS/s3_enable.py`
- [`iam_policy_audit.py`](AWS/iam_policy_audit.py) — Script to analyze AWS IAM policies for security risks (wildcards, overly broad access, best-practice violations). Usage: `python AWS/iam_policy_audit.py <policy_file.json>`
- Terraform config generation
## Features
- Automates key AWS security tasks for better consistency and speed
- Uses Boto3 for live AWS management and can output Terraform for reproducible IaC
## Folder Structure

