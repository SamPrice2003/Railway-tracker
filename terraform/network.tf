################### VPC ###################

data "aws_vpc" "cohort_vpc" {
  id = var.VPC_ID
}

################### Subnets ###################

data "aws_subnets" "public_subnets" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.cohort_vpc.id]
  }

  filter {
    name   = "tag:Name"
    values = ["c21-public-subnet-*"]
  }
}

################### ECS Cluster ###################

data "aws_ecs_cluster" "c21_cluster" {
  cluster_name = var.CLUSTER_NAME
}