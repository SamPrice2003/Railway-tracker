variable "AWS_REGION" {
  type = string
}

variable "AWS_ACCOUNT_ID" {
  type = string
}

variable "CLUSTER_NAME" {
  type = string
}

variable "VPC_ID" {
  type = string
}

variable "PUBLIC_SUBNET_IDS" {
  type = list(string)
}

variable "S3_BUCKET_NAME" {
  type = string
}


variable "LISTENER_IMAGE_URI" {
  type = string
}

variable "DASHBOARD_IMAGE_URI" {
  type = string
}


variable "DASHBOARD_PORT" {
  type    = number
  default = 8501
}

# Database
variable "DB_HOST" {
  type = string
}

variable "DB_PORT" {
  type    = number
  default = 5432
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
