source .env

TERRAFORM_DIR="./terraform"
METRICS_PIPELINE_DIR="./metrics_pipeline"
INCIDENTS_PIPELINE_DIR="./incidents_pipeline"
DASHBOARD_DIR="./dashboard"
REPORT_DIR="./report"

log() {
    echo -e "\n🚂 $1\n"
}


log "🌱 Starting full infrastructure and deployment run..."


log "🌱 Running terraform init..."
cd "$TERRAFORM_DIR"
terraform init


log "🌱 Applying ECR repositories only..."
terraform apply -auto-approve \
    -target=aws_ecr_repository.metrics-pipeline-ecr \
    -target=aws_ecr_repository.incidents-pipeline-ecr \
    -target=aws_ecr_repository.dashboard-ecr \
    -target=aws_ecr_repository.report-ecr

cd ..


log "🌱 Building & pushing pipeline image..."
cd "$METRICS_PIPELINE_DIR"
sh ./dockerise.sh
cd ..


log "🌱 Building & pushing pipeline image..."
cd "$INCIDENTS_PIPELINE_DIR"
sh ./dockerise.sh
cd ..


log "🌱 Building & pushing dashboard image..."
cd "$DASHBOARD_DIR"
sh ./dockerise.sh
cd ..


log "🌱 Building & pushing archive image..."
cd "$REPORT_DIR"
sh ./dockerise.sh
cd ..


log "🌱 Applying remaining resources..."
cd "$TERRAFORM_DIR"
terraform apply -auto-approve


log "🪷 All done! Infrastructure and images are fully deployed."
