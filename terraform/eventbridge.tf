
################### IAM Roles ###################

resource "aws_iam_role" "eventbridge-scheduler-role" {
  name = "c21-railway-tracker-scheduler-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
        Effect = "Allow"
        Principal = {
            Service = "scheduler.amazonaws.com"
        }
        Action = "sts:AssumeRole"
    }]
  })
}

################### Role Policies ###################

resource "aws_iam_role_policy" "eventbridge-metrics-role" {
  policy = jsonencode({
    Statement = [{
        Action = "lambda:InvokeFunction"
        Effect = "Allow"
        Resource = aws_lambda_function.c21-railway-tracker-metrics-lambda.arn
    }]
  })
  role = aws_iam_role.eventbridge-scheduler-role.id
}

resource "aws_iam_role_policy" "eventbridge-metrics-role" {
  policy = jsonencode({
    Statement = [{
        Action = "lambda:InvokeFunction"
        Effect = "Allow"
        Resource = aws_lambda_function.c21-railway-tracker-reports-lambda.arn
    }]
  })
  role = aws_iam_role.eventbridge-scheduler-role.id
}

################### Eventbridge Schedules ###################

resource "aws_scheduler_schedule" "metrics-schedule" {
  name = "c21-railway-tracker-metrics-schedule"

  flexible_time_window {
    mode = "OFF"
  }
  
  schedule_expression = "cron(0 * * * ? *)"

  target {
    arn = aws_lambda_function.c21-railway-tracker-metrics-lambda.arn
    role_arn = aws_iam_role.eventbridge-scheduler-role.arn
  }
}

resource "aws_scheduler_schedule" "report-schedule" {
  name = "c21-railway-tracker-metrics-schedule"

  flexible_time_window {
    mode = "OFF"
  }
  
  schedule_expression = "cron(1 0 * * ? *)"

  target {
    arn = aws_lambda_function.c21-railway-tracker-reports-lambda.arn
    role_arn = aws_iam_role.eventbridge-scheduler-role.arn
  }
}
