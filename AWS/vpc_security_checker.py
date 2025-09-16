import boto3

# Initialize EC2 client
ec2 = boto3.client("ec2")

def check_open_sgs():
    """Detect Security Groups with 0.0.0.0/0 or ::/0 inbound."""
    findings = []
    sgs = ec2.describe_security_groups()["SecurityGroups"]
    for sg in sgs:
        for rule in sg.get("IpPermissions", []):
            for ip_range in rule.get("IpRanges", []):
                if ip_range.get("CidrIp") == "0.0.0.0/0":
                    findings.append(f"SG {sg['GroupId']} allows {rule.get('IpProtocol')} from 0.0.0.0/0")
            for ipv6_range in rule.get("Ipv6Ranges", []):
                if ipv6_range.get("CidrIpv6") == "::/0":
                    findings.append(f"SG {sg['GroupId']} allows {rule.get('IpProtocol')} from ::/0")
    return findings


def check_private_subnets_igw():
    """Detect if private subnets have IGW routes."""
    findings = []
    route_tables = ec2.describe_route_tables()["RouteTables"]

    for rt in route_tables:
        routes = rt.get("Routes", [])
        associations = rt.get("Associations", [])

        for assoc in associations:
            if assoc.get("SubnetId"):  # Only check subnet associations
                subnet_id = assoc["SubnetId"]

                # Get subnet details
                subnet = ec2.describe_subnets(SubnetIds=[subnet_id])["Subnets"][0]
                tags = {t["Key"]: t["Value"] for t in subnet.get("Tags", [])}
                subnet_type = tags.get("Type", "unknown")

                if subnet_type.lower() == "private":
                    for route in routes:
                        if route.get("GatewayId", "").startswith("igw-"):
                            findings.append(f"Private subnet {subnet_id} has route to IGW {route['GatewayId']}")
    return findings


if __name__ == "__main__":
    print("=== Checking Open Security Groups ===")
    sg_findings = check_open_sgs()
    if sg_findings:
        for f in sg_findings:
            print("[ALERT]", f)
    else:
        print("No open SGs detected.")

    print("\n=== Checking Private Subnets with IGW Routes ===")
    subnet_findings = check_private_subnets_igw()
    if subnet_findings:
        for f in subnet_findings:
            print("[ALERT]", f)
    else:
        print("No private subnets with IGW routes detected.")
