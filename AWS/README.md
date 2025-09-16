# AWS Security Tools

This repository contains Python scripts for automating and auditing various AWS security operations.

## Script Summaries

### [ec2_iam_project.py](https://github.com/jibin006/Aws_cloud-security/blob/main/AWS/ec2_iam_project.py)
- **Purpose:** Automates the creation of IAM users and attachment of a specified managed IAM policy. Uses boto3 and prompts for username and policy ARN. Handles errors for both user creation and policy attachment.

### [iam_boto3.py](https://github.com/jibin006/Aws_cloud-security/blob/main/AWS/iam_boto3.py)
- **Purpose:** Provides a simple script to create a new IAM user and attach a selected IAM policy via boto3. It prompts for user input and handles errors in user creation and policy attachment.

### [iam_policy_audit.py](https://github.com/jibin006/Aws_cloud-security/blob/main/AWS/iam_policy_audit.py)
- **Purpose:** Audits all attached managed IAM policies for every IAM user in your account. It fetches and inspects policy JSON to report potentially risky wildcards (like `*` or `s3:*`) in the policy actions, allowing you to detect over-privileged permissions.

### [iamrole_tf.py](https://github.com/jibin006/Aws_cloud-security/blob/main/AWS/iamrole_tf.py)
- **Purpose:** Script likely focused on managing AWS IAM roles, possibly with integration for Terraform-managed resources or related automation functions.

### [s3_enable.py](https://github.com/jibin006/Aws_cloud-security/blob/main/AWS/s3_enable.py)
- **Purpose:** Script, typically for enabling certain security configurations on AWS S3 buckets, such as enforcing encryption, modifying bucket policies, or automated auditing.

### [vpc_security_checker.py](https://github.com/jibin006/Aws_cloud-security/blob/main/AWS/vpc_security_checker.py)
- **Purpose:** Audits VPC-level security, specifically:
  - Detects Security Groups with open inbound rules (0.0.0.0/0 and ::/0).
  - Identifies private subnets that have routes to an Internet Gateway (a common misconfiguration).
  - Prints detailed alerts for each finding to help you improve your VPC security posture.

---

## Usage

- Ensure you have installed `boto3` (`pip install boto3`)
- Configure AWS credentials (`aws configure`)
- Run any script:  
  `python script_name.py`

---

## Security Best Practices

- Always test scripts in non-production environments first.
- Apply least-privilege IAM permissions for script execution.
- Review all code before execution.
- Regularly audit AWS environments using these scripts.

---
