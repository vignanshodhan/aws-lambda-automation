# AWS Lambda - Amazon Aurora RDS Start/Stop Automation

Automatically start or stop an Amazon Aurora RDS cluster using AWS Lambda. This solution helps reduce AWS costs by shutting down non-production databases during off-hours and starting them before business hours.

---

## Features

- Start an Aurora RDS cluster
- Stop an Aurora RDS cluster
- Toggle action based on the current cluster status
- Supports Amazon EventBridge scheduling
- Lightweight Python (boto3) implementation
- Ideal for Development, QA, UAT, and Sandbox environments

---

## Architecture

```
Amazon EventBridge
        │
        ▼
   AWS Lambda
        │
        ▼
Amazon Aurora RDS Cluster
```

---

## Repository Structure

```
rds-start-stop-lambda/
│
├── lambda_function.py
├── requirements.txt
├── README.md
└── iam-policy.json
```

---

## Prerequisites

- Python 3.12+
- AWS Lambda
- Amazon Aurora MySQL or PostgreSQL
- IAM Role with appropriate RDS permissions

---

## IAM Permissions

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeDBClusters",
        "rds:StartDBCluster",
        "rds:StopDBCluster"
      ],
      "Resource": "*"
    }
  ]
}
```

---

## Configuration

Configure the target Aurora cluster using an environment variable.

| Environment Variable | Example |
|----------------------|---------|
| `DB_CLUSTER_IDENTIFIER` | `my-qa-cluster` |

Example:

```text
DB_CLUSTER_IDENTIFIER=my-qa-cluster
```

> **Note:** Avoid hardcoding cluster identifiers in the Lambda function. Using environment variables makes the solution reusable across multiple environments.

---

## Deployment

1. Create an AWS Lambda function.
2. Upload the Python code.
3. Attach an IAM role with the required RDS permissions.
4. Configure the `DB_CLUSTER_IDENTIFIER` environment variable.
5. Create an Amazon EventBridge rule (optional) for scheduled execution.
6. Test the Lambda function.

---

## EventBridge Schedule Examples

### Start Database (Weekdays 9:00 AM IST)

```
cron(30 3 ? * MON-FRI *)
```

### Stop Database (Weekdays 8:00 PM IST)

```
cron(30 14 ? * MON-FRI *)
```

---

## Example Logs

```
Current Status: available
Stopping RDS cluster...
Operation completed successfully.
```

```
Current Status: stopped
Starting RDS cluster...
Operation completed successfully.
```

---

## Cost Optimization

This automation helps reduce AWS costs by stopping non-production Aurora clusters when they are not in use.

Recommended environments:

- Development
- QA
- UAT
- Sandbox
- Testing

---

## Technologies

- AWS Lambda
- Amazon Aurora RDS
- Amazon EventBridge
- Amazon CloudWatch
- Python
- boto3

---


---

## License

This project is licensed under the MIT License.
