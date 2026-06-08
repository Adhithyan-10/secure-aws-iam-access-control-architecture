<div align="center">

# 🔐 Secure AWS IAM Access Control Architecture

### Least Privilege • IAM Roles • Temporary Credentials • IMDSv2 • Serverless Authentication

[![AWS](https://img.shields.io/badge/AWS-Cloud%20Security-orange)]()
[![IAM](https://img.shields.io/badge/IAM-Least%20Privilege-blue)]()
[![Lambda](https://img.shields.io/badge/Lambda-Serverless-yellow)]()
[![DynamoDB](https://img.shields.io/badge/DynamoDB-NoSQL-purple)]()
[![Security](https://img.shields.io/badge/Security-Production%20Focused-green)]()

A hands-on AWS security project demonstrating how modern cloud environments eliminate hardcoded credentials and securely authenticate services using IAM Roles, IMDSv2, and temporary credentials.

</div>

---

# 🏗️ Architecture Overview

<p align="center">
  <img src="./architecture/Archyi.png" alt="Secure AWS IAM Architecture" width="100%">
</p>

---

# 🎯 Project Goal

This project demonstrates how to implement secure AWS access control using:

✅ Least Privilege Access

✅ IAM Users & Groups

✅ IAM Roles

✅ Trust Policies

✅ IMDSv2

✅ Temporary Credentials

✅ Serverless Authentication

✅ Fine-Grained DynamoDB Permissions

✅ CloudWatch Monitoring

The objective was to build a secure authentication flow without relying on long-term AWS access keys.

---

# 🚀 Architecture Flow

```text
IAM User
    │
    ▼
IAM Group + Least Privilege Policy
    │
    ▼
Amazon S3 (Read Only)

──────────────────────────

EC2 Instance
    │
    ▼
IAM Role
    │
    ▼
IMDSv2
    │
    ▼
Temporary Credentials
    │
    ▼
Amazon S3

──────────────────────────

AWS Lambda
    │
    ▼
Lambda Execution Role
    │
    ▼
Amazon DynamoDB
    │
    ▼
CloudWatch Logs
```

---

# 📂 Repository Structure

```text
Secure-AWS-IAM-Access-Control-Architecture
│
├── architecture/
│
├── implementation-walkthrough/
│
├── lambda-code/
│
├── policies/
│
├── cli-commands/
│
├── documentation/
│
└── README.md
```

---

# 📚 Explore Project Resources

## 🏗️ Architecture

Understand the complete security design.

➡️ [View Architecture Documentation](./architecture/README.md)

---

## 📸 Implementation Walkthrough

Complete implementation screenshots and explanations.

➡️ [View Implementation Walkthrough](./implementation-walkthrough/README.md)

---

## ⚡ Lambda Function

Serverless code used for DynamoDB integration.

➡️ [View Lambda Code](./lambda-code/README.md)

---

## 🔐 IAM Policies

All IAM policies used in the project.

➡️ [View Policies](./policies/README.md)

---

## 💻 AWS CLI Commands

Validation and testing commands.

➡️ [View CLI Commands](./cli-commands/README.md)

---

## 📄 Complete Documentation

Full project report.

➡️ [Documentation README](./documentation/README.md)

➡️ [Open PDF Documentation](./documentation/Secure_AWS_IAM_Architecture.pdf)

---

# 🛡️ Security Controls Implemented

| Security Control | Status |
|------------------|---------|
| Least Privilege IAM Policies | ✅ |
| IAM Group-Based Permissions | ✅ |
| IAM Roles | ✅ |
| Trust Relationships | ✅ |
| Temporary Credentials | ✅ |
| IMDSv2 Protection | ✅ |
| Lambda Execution Roles | ✅ |
| Service-to-Service Authentication | ✅ |
| CloudWatch Monitoring | ✅ |
| No Hardcoded Credentials | ✅ |

---

# 🔍 Validation Results

## IAM User Testing

| Action | Result |
|----------|----------|
| List Buckets | ✅ Allowed |
| Read Objects | ✅ Allowed |
| Create Bucket | ❌ Denied |
| Delete Objects | ❌ Denied |
| EC2 Access | ❌ Denied |

---

## EC2 IAM Role Testing

| Action | Result |
|----------|----------|
| List Buckets | ✅ Allowed |
| Read Objects | ✅ Allowed |
| Create Bucket | ❌ Denied |
| Delete Objects | ❌ Denied |

---

## Lambda Testing

| Action | Result |
|----------|----------|
| PutItem | ✅ Allowed |
| GetItem | ✅ Allowed |
| Scan | ✅ Allowed |
| DeleteTable | ❌ Denied |
| UpdateTable | ❌ Denied |

---

# 📈 Project Outcomes

✅ IAM User restricted using least privilege

✅ EC2 accessed S3 using temporary credentials

✅ Unauthorized bucket creation blocked

✅ Lambda successfully inserted records into DynamoDB

✅ No hardcoded credentials used

✅ IMDSv2 used for secure credential retrieval

✅ Secure service-to-service authentication implemented

✅ AWS security best practices applied

---

# 🔮 Future Enhancements

- MFA Enforcement
- AWS Config Rules & Compliance
- IAM Identity Center (SSO)
- AWS Organizations
- Permission Boundaries
- CloudTrail Auditing
- Automated Access Reviews
- Custom Least Privilege Policies

---

# 🧠 Key Cloud Security Learnings

- Never embed AWS credentials inside applications.
- IAM Roles should replace access keys whenever possible.
- Temporary credentials reduce attack surface.
- IMDSv2 protects EC2 metadata access.
- Lambda execution roles enable secure service authentication.
- Least privilege is the foundation of cloud security.
- Fine-grained permissions improve operational security.

---

# 👨‍💻 Author

### Adhithyan Sivaraman T

AWS Student Builder Group Leader

Cloud & DevOps Enthusiast

Federal Institute of Science and Technology (FISAT)

---

<div align="center">

### ⭐ If you found this project useful, consider starring the repository.

**AWS • IAM • Security • Serverless • DevSecOps**

</div>
