################### ECS Cluster ###################

data "aws_ecs_cluster" "c21-cluster" {
  cluster_name = var.CLUSTER_NAME
}

################### CloudWatch Logs ###################

resource "aws_cloudwatch_log_group" "listener" {
  name              = "/ecs/railway-tracker-listener"
  retention_in_days = 7
}

resource "aws_cloudwatch_log_group" "dashboard" {
  name              = "/ecs/railway-tracker-dashboard"
  retention_in_days = 7
}

################### IAM: ECS Execution Role ###################

data "aws_iam_policy_document" "ecs-exec-trust" {
  statement {
    effect = "Allow"
    principals {
      type        = "Service"
      identifiers = ["ecs-tasks.amazonaws.com"]
    }
    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "ecs-exec-role" {
  name               = "c21-railway-tracker-ecs-exec-role"
  assume_role_policy = data.aws_iam_policy_document.ecs-exec-trust.json
}

resource "aws_iam_role_policy_attachment" "ecs-exec-policy-attach" {
  role      = aws_iam_role.ecs-exec-role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

################### Security Groups ###################

resource "aws_security_group" "railway-listener-sg" {
  name        = "c21-railway-tracker-listener-sg"
  description = "Security group for Railway Tracker ECS listener"
  vpc_id = var.VPC_ID

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "railway-dashboard-sg" {
  name        = "c21-railway-tracker-dashboard-sg"
  description = "Security group for Railway Tracker ECS dashboard"
  vpc_id = var.VPC_ID

  ingress {
    from_port   = var.DASHBOARD_PORT
    to_port     = var.DASHBOARD_PORT
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

################### ECS Task Definition: Listener ###################

resource "aws_ecs_task_definition" "railway-listener-task" {
  family                   = "c21-railway-tracker-listener-task"
  requires_compatibilities = ["FARGATE"]
  execution_role_arn       = aws_iam_role.ecs-exec-role.arn
  network_mode             = "awsvpc"
  cpu                      = "256"
  memory                   = "512"

  depends_on = [aws_iam_role_policy_attachment.ecs-exec-policy-attach]

  runtime_platform {
    operating_system_family = "LINUX"
    cpu_architecture        = "X86_64"
  }

  container_definitions = jsonencode([
    {
      name      = "c21-railway-tracker-listener"
      image     = var.LISTENER_IMAGE_URI
      essential = true

      environment = [
        { name = "AWS_REGION", value = var.AWS_REGION },
        { name = "S3_BUCKET",  value = var.S3_BUCKET_NAME },

        { name = "DB_HOST", value = var.DB_HOST },
        { name = "DB_PORT", value = var.DB_PORT },
        { name = "DB_NAME", value = var.DB_NAME },

        { name = "DB_USERNAME", value = var.DB_USERNAME },
        { name = "DB_PASSWORD", value = var.DB_PASSWORD }
      ]

      logConfiguration = {
        logDriver = "awslogs"
        options = {
          awslogs-region        = var.AWS_REGION
          awslogs-group         = aws_cloudwatch_log_group.listener.name
          awslogs-stream-prefix = "ecs"
        }
      }
    }
  ])
}

################### ECS Service: Listener ###################

resource "aws_ecs_service" "railway-listener-service" {
  name             = "c21-railway-tracker-listener-service"
  cluster          = data.aws_ecs_cluster.c21-cluster.id
  task_definition  = aws_ecs_task_definition.railway-listener-task.arn
  launch_type      = "FARGATE"
  platform_version = "LATEST"
  desired_count    = 1
  force_delete     = true

  network_configuration {
    subnets = var.PUBLIC_SUBNET_IDS
    assign_public_ip = true
    security_groups  = [aws_security_group.railway-listener-sg.id]
  }

  lifecycle {
    ignore_changes = [
      desired_count,
      task_definition
    ]
  }
}

################### ECS Task Definition: Dashboard ###################

resource "aws_ecs_task_definition" "railway-dashboard-task" {
  family                   = "c21-railway-tracker-dashboard-task"
  requires_compatibilities = ["FARGATE"]
  execution_role_arn       = aws_iam_role.ecs-exec-role.arn
  network_mode             = "awsvpc"
  cpu                      = "512"
  memory                   = "1024"

  depends_on = [aws_iam_role_policy_attachment.ecs-exec-policy-attach]

  runtime_platform {
    operating_system_family = "LINUX"
    cpu_architecture        = "X86_64"
  }

  container_definitions = jsonencode([
    {
      name      = "c21-railway-tracker-dashboard"
      image     = var.DASHBOARD_IMAGE_URI
      essential = true

      portMappings = [
        {
          containerPort = var.DASHBOARD_PORT
          protocol      = "tcp"
        }
      ]

      environment = [
        { name = "AWS_REGION", value = var.AWS_REGION },
        { name = "S3_BUCKET",  value = var.S3_BUCKET_NAME },

        { name = "DB_HOST", value = var.DB_HOST },
        { name = "DB_PORT", value = var.DB_PORT },
        { name = "DB_NAME", value = var.DB_NAME },

        { name = "DB_USERNAME", value = var.DB_USERNAME },
        { name = "DB_PASSWORD", value = var.DB_PASSWORD }
      ]

      logConfiguration = {
        logDriver = "awslogs"
        options = {
          awslogs-region        = var.AWS_REGION
          awslogs-group         = aws_cloudwatch_log_group.dashboard.name
          awslogs-stream-prefix = "ecs"
        }
      }
    }
  ])
}

################### ECS Service: Dashboard ###################

resource "aws_ecs_service" "railway-dashboard-service" {
  name             = "c21-railway-tracker-dashboard-service"
  cluster          = data.aws_ecs_cluster.c21-cluster.id
  task_definition  = aws_ecs_task_definition.railway-dashboard-task.arn
  launch_type      = "FARGATE"
  platform_version = "LATEST"
  desired_count    = 1
  force_delete     = true

  network_configuration {
    subnets = var.PUBLIC_SUBNET_IDS
    assign_public_ip = true
    security_groups  = [aws_security_group.railway-dashboard-sg.id]
  }

  lifecycle {
    ignore_changes = [
      desired_count,
      task_definition
    ]
  }
}
