# 🏗️ Architecture Overview

The **Secure AWS IAM Access Control Architecture** represents the complete implementation of AWS identity and access management best practices using the principles of **least privilege**, **role-based access control (RBAC)**, and **temporary credentials**.

The architecture is divided into three phases, each demonstrating a different AWS security concept.

## 🖼️ Architecture Diagram

![Secure AWS IAM Access Control Architecture](./Archyi.png)

### Phase 1 – IAM User Security

An IAM user named **developer-user** is added to the **developers** IAM group and granted the **AmazonS3ReadOnlyAccess** managed policy. This ensures that the user can list and read objects from Amazon S3 while being restricted from performing administrative actions such as bucket creation, object deletion, or EC2 access. This phase demonstrates the implementation of the **Least Privilege Principle**.

### Phase 2 – Role-Based Access Control

An EC2 instance is configured with the **EC2-S3-ReadRole** IAM role through a trust relationship that allows the EC2 service to assume the role. Instead of using long-term access keys, the instance securely retrieves **temporary credentials via IAM Role** using **IMDSv2 (Instance Metadata Service Version 2)**. These credentials provide secure, short-lived access to Amazon S3 while eliminating the risks associated with hardcoded credentials.

### Phase 3 – Serverless Data Access

A Lambda function (**dynamodbwriter**) uses a dedicated execution role (**Lambda-DynamoDB-Role**) to securely access a DynamoDB table. The function successfully inserts records into DynamoDB while CloudWatch Logs provide monitoring and auditing capabilities. Permissions are restricted to only the required actions, demonstrating secure service-to-service authentication.

## 🔐 Security Highlights

- Least Privilege Principle
- Role-Based Access Control (RBAC)
- Temporary Credentials via IAM Roles
- IMDSv2 Enabled
- No Hardcoded Credentials
- Service-to-Service Authentication
- Lambda Execution Roles
- Permission Validation & Access Testing
- Secure, Scalable, and Auditable Architecture

## ✅ Project Outcomes

- IAM User restricted using least privilege permissions
- EC2 accessed S3 using temporary credentials
- Unauthorized bucket creation blocked
- Lambda successfully inserted records into DynamoDB
- No hardcoded credentials used
- IMDSv2 used for secure credential retrieval

## 🚀 Future Enhancements

- MFA Enforcement
- CloudTrail Auditing
- IAM Identity Center (SSO)
- Permission Boundaries
- AWS Organizations Integration
- AWS Config Rules & Compliance
- Custom Least Privilege Policies
- Automated Access Reviews
- Multi-Team IAM Governance

---

**Building secure cloud architectures using least privilege, temporary credentials, and role-based access control.**
