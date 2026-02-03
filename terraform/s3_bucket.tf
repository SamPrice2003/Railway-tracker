############### s3 Bucket ###################
resource "aws_s3_bucket" "rail_tracker_archive_bucket" {
  bucket = var.S3_BUCKET_NAME
  force_destroy = true

  tags = {
    Name    = var.S3_BUCKET_NAME
  }
}

################### s3 Bucket Public Access Block ###################
resource "aws_s3_bucket_public_access_block" "rail_tracker_archive_bucket_block" {
  bucket = aws_s3_bucket.archive_bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

################### s3 Bucket Policy ###################
resource "aws_s3_bucket_policy" "rail_tracker_archive_bucket_policy" {
  bucket = aws_s3_bucket.archive_bucket.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Sid       = "PublicReadGetObject"
      Effect    = "Allow"
      Principal = "*"
      Action    = "s3:GetObject"
      Resource = ["arn:aws:s3:::${var.S3_BUCKET_NAME}/*"]
    }]
  })

  depends_on = [aws_s3_bucket_public_access_block.rail_tracker_archive_bucket_block]
}