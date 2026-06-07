# Phase 1 - IAM Security

This phase demonstrates implementation of least-privilege access using IAM users and groups.

## IAM User Creation

![IAM User](1-IAM-User-Creation.png)

Created a restricted IAM user named developer-user.

## IAM Group Creation

![IAM Group](2-IAM-Group-Creation.png)

Created a developers group and attached AmazonS3ReadOnlyAccess policy.

## Login as Restricted User

![Dashboard](3️-developer-user-console-dashboard.png)

Logged in using the restricted IAM user.

## S3 Read Access Verification

![S3 Access](4-S3-Access-Success.png)

Successfully viewed S3 buckets.

## S3 Write Access Denied

![Access Denied](5-S3-Create-Bucket-Access-Denied.png)

Bucket creation failed because write permissions were not granted.

## EC2 Access Denied

![EC2 Denied](6️-ec2-access-denied.png)

EC2 access was blocked due to missing permissions.
