################### IAM Roles ###################

data "aws_iam_policy_document" "lambda_assume_role" {
  statement {
    effect = "Allow"
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "lambda_exec_role" {
  name               = "c21-railway-lambda-exec-role"
  assume_role_policy = data.aws_iam_policy_document.lambda_assume_role.json
}

# Basic CloudWatch logging
resource "aws_iam_role_policy_attachment" "lambda_basic_logs" {
  role       = aws_iam_role.lambda_exec_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

################### S3 Read/Write Policies ###################

data "aws_iam_policy_document" "lambda_s3_policy" {
  statement {
    effect = "Allow"
    actions = [
      "s3:ListBucket"
    ]
    resources = [
      "arn:aws:s3:::${var.S3_BUCKET_NAME}"
    ]
  }

  statement {
    effect = "Allow"
    actions = [
      "s3:GetObject",
      "s3:PutObject",
      "s3:DeleteObject"
    ]
    resources = [
      "arn:aws:s3:::${var.S3_BUCKET_NAME}/*"
    ]
  }
}

resource "aws_iam_policy" "lambda_s3" {
  name   = "c21-railway-tracker-lambda-s3"
  policy = data.aws_iam_policy_document.lambda_s3_policy.json
}

resource "aws_iam_role_policy_attachment" "lambda_s3_attach" {
  role       = aws_iam_role.lambda_exec_role.name
  policy_arn = aws_iam_policy.lambda_s3.arn
}

################### Lambda 1: Metrics Pipeline ###################

resource "aws_lambda_function" "metrics" {
  function_name = "c21-railway-tracker-metrics-pipeline"
  role          = aws_iam_role.lambda_exec_role.arn
  package_type = "Image"
  image_uri    = var.METRICS_LAMBDA_IMAGE_URI
  timeout     = 300
  memory_size = 512

  environment {
    variables = {
      DB_USERNAME = var.DB_USERNAME
      DB_PASSWORD = var.DB_PASSWORD
      DB_HOST     = var.DB_HOST
      DB_NAME     = var.DB_NAME
      DB_PORT     = var.DB_PORT
    }
  }
}

################### Lambda 2: Reporting/Archive ###################

resource "aws_lambda_function" "reports" {
   function_name = "c21-railway-tracker-reports-archiver"
  role          = aws_iam_role.lambda_exec_role.arn
  package_type = "Image"
  image_uri    = var.REPORTS_LAMBDA_IMAGE_URI
  timeout     = 120
  memory_size = 512

  environment {
    variables = {
      S3_BUCKET_NAME = var.S3_BUCKET_NAME
      AWS_ECR_REPO   = var.AWS_ECR_REPORT_REPO
      SOURCE_EMAIL   = var.SOURCE_EMAIL
      DB_USERNAME = var.DB_USERNAME
      DB_PASSWORD = var.DB_PASSWORD
      DB_HOST     = var.DB_HOST
      DB_NAME     = var.DB_NAME
      DB_PORT     = var.DB_PORT
    }
  }
}

