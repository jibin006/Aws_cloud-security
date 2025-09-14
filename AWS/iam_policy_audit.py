''''''''''''''''
🔑 What this script does:
Loops through all IAM users.
For each, fetches attached managed policies.
Downloads the default version of each policy.
Audits it for "Action": "*" or "s3:*" style wildcards.
Prints clear results.

'''''''''''

import boto3

def audit_policy_document(document):
    """
    Audit a single policy document for wildcard actions.
    """
    findings = []

    statements = document.get("Statement", [])
    if isinstance(statements, dict):
        statements = [statements]  # normalize single statement

    for statement in statements:
        actions = statement.get("Action", [])
        if isinstance(actions, str):
            actions = [actions]  # normalize

        for action in actions:
            if action == "*" or action.endswith(":*"):
                findings.append(action)

    return findings 


def audit_user_policies(iam_client, user_name):         
    """
    List attached managed policies for a user and check for wildcards.
    """
    print(f"\n🔍 Auditing user: {user_name}")

    attached_policies = iam_client.list_attached_user_policies(UserName=user_name)["AttachedPolicies"]
    if not attached_policies:
        print("  - No managed policies attached.")
    else:
        for policy in attached_policies:
            arn = policy["PolicyArn"]
            print(f"  - Managed Policy: {policy['PolicyName']} ({arn})")

            # Get default version of the managed policy
            version = iam_client.get_policy(PolicyArn=arn)["Policy"]["DefaultVersionId"]
            policy_version = iam_client.get_policy_version(
                PolicyArn=arn,
                VersionId=version
            )["PolicyVersion"]["Document"]

            # Audit the document
            findings = audit_policy_document(policy_version)
            if findings:
                print(f"    ⚠️ Wildcard actions found: {findings}")
            else:
                print("    ✅ No wildcards found.")


def main():
    iam = boto3.client("iam")

    # Get all users
    users = iam.list_users()["Users"]
    for user in users:
        user_name = user["UserName"]
        audit_user_policies(iam, user_name)


if __name__ == "__main__":
    main()




''''''''''''''''

🔍 Walkthrough of the script line by line
import boto3

This imports the AWS SDK for Python (boto3).
Without this, you can’t talk to AWS.

def audit_policy_document(document):

This is a function that checks one policy document.
Think of it as a “policy scanner.”

    statements = document.get("Statement", [])
    if isinstance(statements, dict):
        statements = [statements]

A policy has one or more "Statement" blocks.
Sometimes AWS returns a single block (a dict), sometimes a list.
This code makes sure it’s always a list, so we can loop without errors.

    for statement in statements:
        actions = statement.get("Action", [])
        if isinstance(actions, str):
            actions = [actions]


Each statement has actions.
Same trick: sometimes it’s "s3:*", sometimes it’s ["s3:GetObject", "s3:PutObject"].
We normalize it so it’s always a list.

        for action in actions:
            if action == "*" or action.endswith(":*"):
                findings.append(action)


Loop through all actions.
If action is "*" (everything) or ends with :* (like "s3:*") → mark it as risky.
findings = list of bad actions found.

def audit_user_policies(iam_client, user_name):
    attached_policies = iam_client.list_attached_user_policies(UserName=user_name)["AttachedPolicies"]


This function is for a user.
First, it asks AWS: “Hey, what managed policies are attached to this user?”
AWS replies with a list.

            arn = policy["PolicyArn"]
            version = iam_client.get_policy(PolicyArn=arn)["Policy"]["DefaultVersionId"]
            policy_version = iam_client.get_policy_version(
                PolicyArn=arn,
                VersionId=version
            )["PolicyVersion"]["Document"]


Each policy has an ARN (unique ID).
Policies have versions; we grab the default version.
Then we fetch the actual JSON policy document to inspect it.

            findings = audit_policy_document(policy_version)


Now we pass that JSON into our earlier “scanner function.”
If it finds wildcards, it returns them.

def main():
    iam = boto3.client("iam")
    users = iam.list_users()["Users"]


iam = boto3.client("iam") → creates a connection to IAM.

list_users() → asks AWS: “Who are all the users in this account?”

    for user in users:
        user_name = user["UserName"]
        audit_user_policies(iam, user_name)


For each user in that list, we run our audit function.
So it checks every single IAM user automatically.

if __name__ == "__main__":
    main()


This is just Python’s way of saying “run main() if this file is executed.”

✅ So, line by line:

main() → list users.
audit_user_policies() → grab their managed policies.
audit_policy_document() → check inside each policy for wildcards.

'''''''''''
