# AWS CLI Commands

## Overview

This document contains the AWS CLI and Linux commands used throughout the Secure AWS IAM Access Control Architecture project.

The commands were used to validate IAM permissions, retrieve temporary credentials using IMDSv2, and verify access controls.

---

# 1. List S3 Buckets

Used to verify read access from EC2 through the attached IAM Role.

```bash
aws s3 ls
```

Expected Result:

- Bucket listing successful
- Read-only permissions validated

---

# 2. Generate IMDSv2 Token

Used to securely communicate with the EC2 Instance Metadata Service Version 2.

```bash
TOKEN=$(curl -X PUT \
"http://169.254.169.254/latest/api/token" \
-H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
```

Expected Result:

- Temporary IMDSv2 token generated

---

# 3. Retrieve IAM Role Name

Used to verify that the EC2 instance successfully assumed the attached IAM Role.

```bash
curl -H "X-aws-ec2-metadata-token: $TOKEN" \
http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

Expected Result:

- IAM Role name displayed

Example:

```text
EC2-S3-ReadRole
```

---

# 4. Retrieve Temporary Credentials

Used to inspect temporary credentials provided by IAM Roles.

```bash
curl -H "X-aws-ec2-metadata-token: $TOKEN" \
http://169.254.169.254/latest/meta-data/iam/security-credentials/EC2-S3-ReadRole
```

Expected Result:

- Temporary Access Key
- Temporary Secret Key
- Session Token

---

# 5. Attempt Bucket Creation

Used to validate least privilege restrictions.

```bash
aws s3 mb s3://test-bucket-name
```

Expected Result:

```text
AccessDenied
```

This confirms that write permissions were not granted.

---

# Security Concepts Demonstrated

- IAM Roles
- Temporary Credentials
- IMDSv2
- Least Privilege
- AWS CLI Authentication
- Access Validation Testing

---

# Outcome

The AWS CLI commands successfully validated IAM permissions, role assumption, temporary credential retrieval, and access restrictions throughout the project.
