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

################### IAM: ECS Task Roles ###################

# task role for ecs
resource "aws_iam_role" "ecs-task-definition-role" {
  name = "c21-railway-tracker-ecs-role"

  lifecycle {
    create_before_destroy = true
  }

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "ecs-tasks.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })
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

################### ECS Task Definitions ###################

# task definition listener
resource "aws_ecs_task_definition" "railway-listener-task" {
  family                   = "c21-railway-tracker-listener-task"
  requires_compatibilities = ["FARGATE"]
  task_role_arn            = aws_iam_role.ecs-task-definition-role.arn
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
      name         = "c21-railway-tracker-listener"
      image        = var.LISTENER_IMAGE_URI
      cpu          = 0
      portMappings = []
      essential    = true

      environment = [
        { name = "S3_BUCKET",  value = var.S3_BUCKET_NAME },
        { name = "AWS_REGION",  value = var.AWS_REGION },
        { name = "STOMP_PASSWORD",  value = var.STOMP_PASSWORD },
        { name = "DB_PORT", value = var.DB_PORT },
        { name = "DB_NAME", value = var.DB_NAME },
        { name = "STOMP_TOPIC",  value = var.STOMP_TOPIC },
        { name = "STOMP_PORT",  value = var.STOMP_PORT },
        { name = "DB_HOST", value = var.DB_HOST },
        { name = "STOMP_USERNAME",  value = var.STOMP_USERNAME },
        { name = "DB_USERNAME", value = var.DB_USERNAME },
        { name = "AWS_ECR_INCIDENTS_REPO",  value = var.AWS_ECR_INCIDENTS_REPO },
        { name = "STOMP_HOST",  value = var.STOMP_HOST },
        { name = "AWS_SECRET_KEY",  value = var.AWS_SECRET_ACCESS_KEY },
        { name = "SNS_TOPIC",  value = var.SNS_TOPIC },
        { name = "AWS_ACCESS_KEY",  value = var.AWS_ACCESS_KEY_ID },
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

# task definition dashboard
resource "aws_ecs_task_definition" "railway-dashboard-task" {
  family                   = "c21-railway-tracker-dashboard-task"
  requires_compatibilities = ["FARGATE"]
  task_role_arn            = aws_iam_role.ecs-task-definition-role.arn
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
      name         = "c21-railway-tracker-listener"
      image        = var.LISTENER_IMAGE_URI
      cpu          = 0
      portMappings = []
      essential    = true

      environment = [
        { name = "AWS_REGION",  value = var.AWS_REGION },
        { name = "DB_PORT", value = var.DB_PORT },
        { name = "DB_NAME", value = var.DB_NAME },
        { name = "DB_HOST", value = var.DB_HOST },
        { name = "DB_USERNAME", value = var.DB_USERNAME },
        { name = "AWS_ECR_DASHBOARD_REPO",  value = var.AWS_ECR_INCIDENTS_REPO },
        { name = "AWS_SECRET_KEY",  value = var.AWS_SECRET_ACCESS_KEY },
        { name = "AWS_ACCESS_KEY",  value = var.AWS_ACCESS_KEY_ID },
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
  cluster = data.aws_ecs_cluster.c21_cluster.id
  task_definition  = aws_ecs_task_definition.railway-listener-task.arn
  launch_type      = "FARGATE"
  platform_version = "LATEST"
  desired_count    = 1
  force_delete     = true

  network_configuration {
    subnets = data.aws_subnets.public_subnets.ids
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

################### ECS Service: Dashboard ###################

resource "aws_ecs_service" "railway-dashboard-service" {
  name             = "c21-railway-tracker-dashboard-service"
  cluster = data.aws_ecs_cluster.c21_cluster.id
  task_definition  = aws_ecs_task_definition.railway-dashboard-task.arn
  launch_type      = "FARGATE"
  platform_version = "LATEST"
  desired_count    = 1
  force_delete     = true

  network_configuration {
    subnets = data.aws_subnets.public_subnets.ids
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
