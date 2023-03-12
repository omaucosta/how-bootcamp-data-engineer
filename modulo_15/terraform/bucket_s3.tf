provider "aws" {
    profile = "default"
    region = "us-east-1"  
}

resource "aws_s3_bucket" "bucket-prod" {
    bucket = "bucket-sandbpx-prod"
    tags = {
        "Area" = "Produtos"
        "Enviroment" = "Production"
    }
}

resource "aws_s3_bucket" "bucket-dev" {
    bucket = "bucket-sandbpx-dev"
    tags = {
        "Area" = "Produtos"
        "Enviroment" = "Development"
    }
}