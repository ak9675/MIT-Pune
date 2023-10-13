provider "aws" {
 region = "us-east-1"
 access_key = "AKIAYD6BO3N5BQZVX73R"
 secret_key = "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"
}

resource "aws_instance" "web" {
  ami           = "ami-041feb57c611358bd"
  instance_type = "t3.micro"

  tags = {
    Name = "MITVM"
  }
}