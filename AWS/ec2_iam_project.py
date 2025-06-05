instance_name = input("Enter the EC2 instance name: ")
ami_id = input("Enter the AMI ID (e.g., ami-0abcdef1234567890): ")
instance_type = input("Enter the EC2 instance type (e.g., t2.micro): ")
role_name = input("Enter the IAM role name: ")
policy_arn = input("Enter the managed policy ARN (e.g., arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess): ")


with open("main.tf", "w") as f:
    f.write(f'''
resource "aws_iam_role" "my_role" {{
  name = "{role_name}"
  assume_role_policy = jsonencode({{
    "Version": "2012-10-17",
    "Statement": [
      {{
        "Effect": "Allow",
        "Principal": {{
          "Service": "ec2.amazonaws.com"
        }},
        "Action": "sts:AssumeRole"
      }}
    ]
  }})
}}

resource "aws_iam_role_policy_attachment" "attach_policy" {{
  role       = aws_iam_role.my_role.name
  policy_arn = "{policy_arn}"
}}

resource "aws_instance" "my_ec2" {{
  ami                    = "{ami_id}"
  instance_type          = "{instance_type}"
  iam_instance_profile   = aws_iam_instance_profile.my_profile.name
  tags = {{
    Name = "{instance_name}"
  }}
}}

resource "aws_iam_instance_profile" "my_profile" {{
  name = "{role_name}_profile"
  role = aws_iam_role.my_role.name
}}
''')
