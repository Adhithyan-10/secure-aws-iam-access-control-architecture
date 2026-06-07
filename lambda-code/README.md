# AWS Lambda Function

## Overview

This Lambda function demonstrates secure serverless access to Amazon DynamoDB using IAM Execution Roles.

Instead of storing AWS credentials inside the code, AWS Lambda automatically assumes an execution role and receives temporary credentials at runtime.

This follows AWS security best practices and eliminates the need for hardcoded access keys.

---

## AWS Services Used

- AWS Lambda
- Amazon DynamoDB
- AWS IAM
- Amazon CloudWatch Logs

---

## Workflow

1. Lambda function is invoked.
2. Lambda assumes its execution role.
3. Temporary credentials are provided automatically.
4. The function writes data to DynamoDB.
5. Execution logs are stored in CloudWatch Logs.

---

## Security Features

- No hardcoded AWS credentials
- Least Privilege IAM permissions
- Role-Based Authentication
- Temporary Credentials
- CloudWatch Logging

---

## Outcome

The Lambda function successfully inserted records into DynamoDB using IAM Role-based authentication.
