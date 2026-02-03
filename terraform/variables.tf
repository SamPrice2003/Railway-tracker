variable "AWS_REGION" {
  type = string
}

variable "AWS_ACCOUNT_ID" {
  type = string
}

variable "VPC_ID" {
  type = string
}

variable "CLUSTER_NAME" {
  type = string
}

variable "DB_HOST" {
  type = string
}

variable "DB_NAME" {
  type = string
}

variable "DB_USERNAME" {
  type = string
}

variable "DB_PASSWORD" {
  type      = string
  sensitive = true
}

variable "S3_BUCKET_NAME" {
  type = string
}
