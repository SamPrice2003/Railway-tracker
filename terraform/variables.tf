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

variable "S3_BUCKET_NAME" {
  type = string
}

variable "ECS_IMAGE_URI" {
  type = string
}

variable "AWS_ACCESS_KEY_ID" {
  type      = string
  sensitive = true
}

variable "AWS_SECRET_ACCESS_KEY" {
  type      = string
  sensitive = true
}
