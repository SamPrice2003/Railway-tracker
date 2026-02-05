################### VPC ###################

data "aws_vpc" "cohort_vpc" {
  id = var.VPC_ID
}

################### Public Subnets ###################

data "aws_subnets" "public_subnets" {
  filter {
    name   = "vpc-id"
    values = [var.VPC_ID]
  }

  filter {
    name   = "map-public-ip-on-launch"
    values = ["true"]
  }
}

################### ECS Cluster ###################

data "aws_ecs_cluster" "c21_cluster" {
  cluster_name = var.CLUSTER_NAME
}
