# AWS Security Tools

This directory contains various AWS security scripts and tools for monitoring and auditing AWS infrastructure.

## Scripts Overview

### vpc_security_checker.py
A comprehensive VPC security auditing tool that checks for common security misconfigurations:

**Features:**
- Detects Security Groups with overly permissive inbound rules (0.0.0.0/0 or ::/0)
- Identifies private subnets that incorrectly have Internet Gateway routes
- Provides detailed alerts for security findings

**Usage:**
```bash
python vpc_security_checker.py
```

**Prerequisites:**
- AWS credentials configured (via AWS CLI, environment variables, or IAM roles)
- boto3 library installed: `pip install boto3`
- Appropriate IAM permissions to read VPC, Security Group, and Route Table information

**Sample Output:**
```
=== Checking Open Security Groups ===
[ALERT] SG sg-1234567890abcdef0 allows tcp from 0.0.0.0/0
[ALERT] SG sg-0987654321fedcba0 allows -1 from ::/0

=== Checking Private Subnets with IGW Routes ===
[ALERT] Private subnet subnet-1234567890abcdef0 has route to IGW igw-1234567890abcdef0
```

### Other Scripts
- **ec2_iam_project.py** - EC2 and IAM management utilities
- **iam_boto3.py** - IAM operations using boto3
- **iam_policy_audit.py** - IAM policy auditing tool
- **iamrole_tf.py** - IAM role management with Terraform integration
- **s3_enable.py** - S3 security configuration tool

## Getting Started

1. Install required dependencies:
   ```bash
   pip install boto3
   ```

2. Configure AWS credentials:
   ```bash
   aws configure
   ```

3. Run any script:
   ```bash
   python <script_name>.py
   ```

## Security Best Practices

- Always test scripts in a non-production environment first
- Ensure proper IAM permissions are configured with least privilege principle
- Review and understand each script before execution
- Regularly audit your AWS infrastructure using these tools

## Contributing

Feel free to contribute improvements or additional security tools to this collection.
