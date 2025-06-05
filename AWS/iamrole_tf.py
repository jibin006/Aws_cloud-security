# ✅ Step 1: Ask the user for the role name and policy ARN
role_name = input("Enter the IAM role name: ")
policy_arn = input("Enter the managed policy ARN: ")

# ✅ Step 2: Open (or create) a file named main.tf for writing
with open("main.tf", "w") as f:
    
    # ✅ Step 3: Write the Terraform configuration into the file
    f.write(f'''
resource "aws_iam_role" "my_role" {{
  name = "{role_name}"

  assume_role_policy = jsonencode({{
    "Version": "2012-10-17",
    "Statement": [
      {{
        "Action": "sts:AssumeRole",
        "Effect": "Allow",
        "Principal": {{
          "Service": "ec2.amazonaws.com"
        }}
      }}
    ]
  }})
}}

resource "aws_iam_role_policy_attachment" "attach_policy" {{
  role       = aws_iam_role.my_role.name
  policy_arn = "{policy_arn}"
}}
''')

