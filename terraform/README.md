# Terraform Information

This folder provisions the AWS infrastructure for the Railway Tracker project using Terraform.

## What this Terraform creates

- VPC networking dependencies (uses your existing VPC + subnets)
- S3 bucket for pipeline outputs and report archives
- ECS Fargate services:
  - Listener service (live updates listener)
  - Dashboard service (web dashboard)
- Lambda functions (container image based, pulled from ECR):
  - Metrics pipeline Lambda
  - Reports and archive Lambda


## Repository Structure

- `provider.tf`  
  Configures the AWS provider (region and authentication).

- `network.tf`  
  References networking resources (VPC and subnets) used by ECS services.

- `s3_bucket.tf`  
  Creates the S3 bucket used by the project.

- `ecs.tf`  
  Defines ECS task definitions, services, security groups, and CloudWatch log groups.

- `variables.tf`  
  Declares all input variables required by the Terraform configuration, including AWS settings, networking details, image URIs, database credentials, and service configuration values.

- `terraform.tfvars`  
  Provides concrete values for the variables declared in `variables.tf`, allowing environment specific configuration without modifying the Terraform code.


## Prerequisites

You must have:

- Terraform installed 
- An existing AWS VPC and at least two public subnets in the same VPC
- ECR repositories created for:
  - Listener image
  - Dashboard image
  - Metrics Lambda image
  - Reports Lambda image
- Docker installed (to build and push images to ECR)
- RDS instance created (or created elsewhere in Terraform) with connection details available


## Setup

### 1. Create a file named terraform.tfvars in this folder and populate it with your environment values, the required values are listed below:

```
AWS_REGION  = "<your_aws_region>"
VPC_ID = "<your_aws_VPC_ID>"
CLUSTER_NAME = "<your_aws_cluster_name>"
AWS_ACCOUNT_ID = "<your_aws_account_id>"
AWS_ACCESS_KEY_ID = "<your_aws_access_key_id>"
AWS_SECRET_ACCESS_KEY = "<your_aws_secret_access_key>"

PUBLIC_SUBNET_IDS = ["<your_aws_public_subnet_1>","<your_aws_public_subnet_1>"]

LISTENER_IMAGE_URI  = "<your_ecr_uri>"
DASHBOARD_IMAGE_URI = "<your_ecr_uri>"
METRICS_LAMBDA_IMAGE_URI = "<your_ecr_uri>"
REPORTS_LAMBDA_IMAGE_URI = "<your_ecr_uri>"

S3_BUCKET_NAME = "<your_s3_bucket_name>"

DASHBOARD_PORT = 8501

DB_HOST     = "<your_db_host>"
DB_PORT     = "<your_db_port>"
DB_NAME     = "<your_db_name>"
DB_USERNAME = "<your_db_username>"
DB_PASSWORD = "<your_db_password>"
```

Notes:

- PUBLIC_SUBNET_IDS must contain subnet IDs in the same VPC.

- Image URIs must include a tag, for example :latest.

- DB_PASSWORD should be treated as sensitive and must not be committed.


### 2. Build and push images to ECR (required before terraform apply)

ECS and Lambda will fail to deploy if the ECR images do not exist.

Make sure the following image URIs in terraform.tfvars point to real images in ECR:

- LISTENER_IMAGE_URI

- DASHBOARD_IMAGE_URI

- METRICS_LAMBDA_IMAGE_URI

- REPORTS_LAMBDA_IMAGE_URI

You can confirm images exist with:

```
aws ecr list-images --repository-name <repo-name> --region <region>
```

### 3. Once all files are created and configured correctly, initialise Terraform:
```
terraform init
```

### 4. Validate configuration:
```
terraform validate
```

### 5. Plan changes:
```
terraform plan
```

### 6. Apply: 
```
terraform apply
```

## Verifying Deployment

### ECS 

AWS Console -> ECS -> Cluster -> Services
Both services should show ```RUNNING (1/1)```

If a task is failing:

ECS -> Tasks -> select failed task -> view “Stopped reason”

CloudWatch -> Log groups:

    - /ecs/railway-tracker-listener

    - /ecs/railway-tracker-dashboard

### Dashboard

If your dashboard is deployed with a public IP, find it via:
ECS -> Tasks -> Dashboard task -> Networking -> Public IP

Then open: 
```
http://<PUBLIC_IP>:8501
```

### Lambda

AWS Console -> Lambda -> Functions

    - c21-railway-tracker-metrics-pipeline

    - c21-railway-tracker-reports-archiver


## Common Issues

### Lambda error: “Source image … does not exist”

Cause: the ECR image/tag referenced in *_LAMBDA_IMAGE_URI does not exist.
Fix: build and push the image to the exact repository and tag.

### ECS error: “CannotPullContainerError”

Cause: the ECR URI is wrong or the image was never pushed.
Fix: verify the repo name, region, and tag, then push the image.

### DB connection timeouts

Cause: RDS security group does not allow inbound from ECS task security group, or wrong port/host.
Fix: allow inbound from ECS SG to the DB port and verify ```DB_HOST/DB_PORT```.


## Security Notes

Add terraform.tfvars to .gitignore:

    - terraform.tfvars

Avoid committing DB credentials. Use Secrets Manager.



## Destroying Resources

To delete all resources created by this Terraform:

    - terraform destroy
