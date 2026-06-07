# AWS Lambda Function

## 🔗 Quick Access

- [View Lambda Function Code](./lambda-function.py)

---

## Overview

This Lambda function demonstrates secure serverless access to Amazon DynamoDB using IAM Execution Roles.

Instead of storing AWS credentials inside the application code, AWS Lambda automatically assumes an execution role and receives temporary credentials at runtime.

This follows AWS security best practices and eliminates the need for hardcoded access keys.

---

## AWS Services Used

- AWS Lambda
- Amazon DynamoDB
- AWS IAM
- Amazon CloudWatch Logs

---

## Function Workflow

1. Lambda function is invoked.
2. Lambda automatically assumes its execution role.
3. Temporary credentials are provided through the execution role.
4. The function inserts data into the DynamoDB table.
5. Execution logs are generated in CloudWatch Logs.

---

## Security Features

### IAM Execution Role

The Lambda function does not use:

- Access Keys
- Secret Keys
- Hardcoded Credentials

Instead, AWS automatically provides temporary credentials through the assigned execution role.

### Least Privilege Principle

The role only contains permissions required to:

- Insert records into DynamoDB
- Read records from DynamoDB
- Write logs to CloudWatch

---

## Sample Record

```json
{
  "userId": "1",
  "name": "Adhithyan"
}
```

---

## Outcome

The Lambda function successfully inserted records into DynamoDB using IAM Role-based authentication.

This demonstrates secure serverless access control without exposing AWS credentials.

---

## Source Code

📄 **Lambda Function:**  
[lambda_function.py](./lambda_function.py)
