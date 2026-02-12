################### ECR REPOSITORIES ###################

# repo for the metrics pipeline lambda function
resource "aws_ecr_repository" "metrics-pipeline-ecr" {
  name                 = "c21-railway-tracker-metrics-pipeline"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  force_delete = true
}

# repo for the incidents pipeline ECS task definition
resource "aws_ecr_repository" "incidents-pipeline-ecr" {
  name                 = "c21-railway-tracker-incidents-pipeline"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  force_delete = true
}

# repo for the dashboard ECS task definition
resource "aws_ecr_repository" "dashboard-ecr" {
  name                 = "c21-railway-tracker-dashboard"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  force_delete = true
}

# repo for the report/archive lambda function
resource "aws_ecr_repository" "report-ecr" {
  name                 = "c21-railway-tracker-report"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  force_delete = true
}

################### ECR IMAGES ###################

# references the metrics pipeline ecr image
data "aws_ecr_image" "" {
  repository_name = aws_ecr_repository.metrics-pipeline-ecr.name
  image_tag       = "latest"
}

# references the incidents pipeline ecr image
data "aws_ecr_image" "" {
  repository_name = aws_ecr_repository.incidents-pipeline-ecr.name
  image_tag       = "latest"
}

# references the dashboard ecr image
data "aws_ecr_image" "" {
  repository_name = aws_ecr_repository.dashboard-ecr.name
  image_tag       = "latest"
}

# references the report/archive ecr image
data "aws_ecr_image" "" {
  repository_name = aws_ecr_repository.report-ecr.name
  image_tag       = "latest"
}

