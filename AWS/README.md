# AWS Security Tools

This directory contains various AWS security scripts and tools for monitoring and auditing AWS infrastructure.

## Scripts Overview

• **ec2_iam_project.py** - EC2 and IAM management utilities
• **iam_boto3.py** - IAM operations using boto3
• **iam_policy_audit.py** - IAM policy auditing tool
• **iamrole_tf.py** - IAM role management with Terraform integration
• **s3_enable.py** - S3 security configuration tool

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
