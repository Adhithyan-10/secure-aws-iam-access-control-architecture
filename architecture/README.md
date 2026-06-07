# 🏗️ Architecture Overview

The **Secure AWS IAM Access Control Architecture** represents the complete implementation of AWS identity and access management best practices using the principles of **least privilege**, **role-based access control (RBAC)**, and **temporary credentials**.

The architecture is divided into three phases, each demonstrating a different AWS security concept.

### Phase 1 – IAM User Security

An IAM user named **developer-user** is added to the **developers** IAM group and granted the **AmazonS3ReadOnlyAccess** managed policy. This ensures that the user can list and read objects from Amazon S3 while being restricted from performing administrative actions such as bucket creation, object deletion, or EC2 access. This phase demonstrates the implementation and validation of the **least privilege principle**.

### Phase 2 – Role-Based Access Control

An EC2 instance is configured with an IAM role (**EC2-S3-ReadRole**) through a trust relationship that allows the EC2 service to assume the role. Instead of using long-term access keys, the instance securely retrieves **temporary credentials via IAM Role** using **IMDSv2 (Instance Metadata Service Version 2)**. These short-lived credentials provide controlled access to Amazon S3 while reducing the security risks associated with static credentials. This phase demonstrates secure role assumption, credential rotation, and role-based access management.

### Phase 3 – Serverless Data Access

A Lambda function (**dynamodbwriter**) is configured with a dedicated execution role (**Lambda-DynamoDB-Role**) that grants controlled access to a DynamoDB table. The Lambda function successfully writes records to DynamoDB while all activities are monitored through **CloudWatch Logs**. Permissions are restricted to only the required DynamoDB operations, ensuring secure service-to-service authentication without exposing credentials. This phase demonstrates secure serverless access control and monitoring.

### Security Highlights

The architecture follows multiple AWS security best practices:

- Least Privilege Principle
- Role-Based Access Control (RBAC)
- Temporary Credentials via IAM Roles
- IMDSv2 Enabled
- No Hardcoded Credentials
- Service-to-Service Authentication
- Lambda Execution Roles
- Permission Validation & Access Testing
- Secure, Scalable, and Auditable Design

### Key Outcomes

Through this implementation:

- IAM users were restricted using least privilege permissions.
- EC2 instances accessed S3 using temporary credentials instead of access keys.
- Unauthorized bucket creation and deletion operations were successfully blocked.
- Lambda functions securely inserted records into DynamoDB.
- No hardcoded AWS credentials were used.
- IMDSv2 was implemented for secure credential retrieval.
- CloudWatch logging was enabled for monitoring and auditing.

This architecture demonstrates a practical, real-world AWS security implementation that combines IAM Users, IAM Groups, IAM Roles, Trust Policies, IMDSv2, AWS Lambda, DynamoDB, and CloudWatch to build a secure and scalable cloud environment.
