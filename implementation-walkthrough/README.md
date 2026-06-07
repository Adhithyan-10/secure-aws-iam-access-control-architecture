# Implementation Walkthrough

## Overview

This section documents the complete implementation of the **Secure AWS IAM Access Control Architecture** project.

The project demonstrates how AWS Identity and Access Management (IAM) can be used to implement secure access control through users, groups, roles, temporary credentials, and serverless service-to-service authentication.

The implementation is divided into three phases that progressively build a secure AWS environment.

---

## Phase 1: IAM Security

📁 **phase-1-iam-security**

This phase focuses on implementing the Principle of Least Privilege using IAM users and groups.

### Activities Performed

* Created a restricted IAM user (`developer-user`)
* Created an IAM group (`developers`)
* Attached Amazon S3 ReadOnly permissions
* Logged in as the restricted user
* Verified successful S3 read access
* Verified denial of unauthorized actions
* Validated access restrictions for EC2 resources

### Key Concepts

* IAM Users
* IAM Groups
* Permission Policies
* Least Privilege Access Control

---

## Phase 2: Role-Based Access

📁 **phase-2-role-based-access**

This phase demonstrates secure access to AWS services using IAM Roles and temporary credentials instead of long-term access keys.

### Activities Performed

* Created an IAM Role for EC2
* Attached S3 ReadOnly permissions to the role
* Launched an EC2 instance with the role attached
* Verified credentials using IMDSv2
* Accessed S3 from EC2 using AWS CLI
* Validated write-access restrictions

### Key Concepts

* IAM Roles
* Instance Profiles
* Temporary Credentials
* IMDSv2
* Role-Based Authentication

---

## Phase 3: Serverless Access

📁 **phase-3-serverless-access**

This phase demonstrates secure service-to-service communication using AWS Lambda and DynamoDB.

### Activities Performed

* Created a DynamoDB table
* Created a Lambda execution role
* Granted DynamoDB permissions to Lambda
* Developed and deployed a Python Lambda function
* Executed test events
* Verified successful data insertion into DynamoDB

### Key Concepts

* AWS Lambda
* DynamoDB
* Execution Roles
* Service-to-Service Authentication
* Serverless Security

---

## Security Outcomes Achieved

✔ Enforced Principle of Least Privilege

✔ Restricted unauthorized AWS service access

✔ Eliminated the need for hardcoded access keys

✔ Implemented temporary credential-based authentication

✔ Secured EC2-to-S3 communication using IAM Roles

✔ Secured Lambda-to-DynamoDB communication using Execution Roles

✔ Demonstrated modern AWS identity and access management practices

---

## Learning Outcomes

Through this implementation, the following AWS security concepts were successfully demonstrated:

* IAM User and Group Management
* Policy-Based Access Control
* IAM Roles and Trust Relationships
* EC2 Instance Profiles
* IMDSv2 Authentication
* AWS CLI Authentication Using Roles
* Serverless Security Architecture
* DynamoDB Integration with Lambda
* Principle of Least Privilege Implementation

---

## Project Flow

```text
IAM User & Group
        │
        ▼
Permission Validation
        │
        ▼
EC2 IAM Role
        │
        ▼
Temporary Credentials (IMDSv2)
        │
        ▼
S3 Read-Only Access
        │
        ▼
Lambda Execution Role
        │
        ▼
DynamoDB Access
```

This walkthrough provides a complete demonstration of secure identity and access management practices in AWS using both traditional and serverless architectures.

