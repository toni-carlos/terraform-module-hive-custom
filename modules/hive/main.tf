terraform {
  required_version = "1.2.7"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.27.0"
    }
  }
}


data "template_file" "file" {
  template = "${file("${path.module}/../../${var.path_file}")}"
}

resource "null_resource" "hive_connect" {
  triggers = {
    file_changed = md5(data.template_file.file.rendered)
  }

  provisioner "local-exec" {
    command = "chmod +x ${path.module}/run.sh | ${path.module}/run.sh -f ${var.path_file}"
  }
}