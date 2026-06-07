# IAM Policies

## Overview

This folder contains the IAM policies used throughout the Secure AWS IAM Access Control Architecture project.

The policies demonstrate the implementation of the Principle of Least Privilege by granting only the permissions required for specific tasks.

---

## Available Policies

### 1. S3 Read-Only Policy

📄 File: [s3-readonly-policy.json](./s3-readonly-policy.json)

Purpose:

- Allow listing S3 buckets
- Allow reading objects
- Deny bucket creation
- Deny object deletion
- Prevent unauthorized modifications

Used By:

- IAM Group (developers)
- EC2 IAM Role (EC2-S3-ReadRole)

---

### 2. Lambda DynamoDB Policy

📄 File: [lambda-dynamodb-policy.json](./lambda-dynamodb-policy.json)

Purpose:

- Allow Lambda to insert records into DynamoDB
- Allow reading records
- Enable controlled access to the userdata table

Used By:

- Lambda Execution Role

---

## Security Principles Implemented

- Least Privilege Access
- Role-Based Authentication
- Temporary Credential Usage
- Service-to-Service Authorization
- No Hardcoded Credentials

---

## Outcome

These policies ensure that users, EC2 instances, and Lambda functions receive only the permissions necessary to perform their intended tasks.
