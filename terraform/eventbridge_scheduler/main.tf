data "aws_lambda_function" "main" {
  function_name = "print_time"
}

data "aws_iam_policy_document" "main" {
  statement {
    actions = ["lambda:InvokeFunction"]
    resources = [
      "${data.aws_lambda_function.main.arn}:*",
      data.aws_lambda_function.main.arn
    ]
  }
}

data "aws_iam_policy_document" "assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["scheduler.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "main" {
  assume_role_policy = data.aws_iam_policy_document.assume_role_policy.json
}

resource "aws_iam_role_policy" "main" {
  policy = data.aws_iam_policy_document.main.json
  role   = aws_iam_role.main.id
}

resource "aws_scheduler_schedule" "main" {
  schedule_expression = "rate(1 hour)"
  name                = "my_hourly_schedule"
  flexible_time_window {
    mode = "OFF"
  }
  target {
    arn      = data.aws_lambda_function.main.arn
    role_arn = aws_iam_role.main.arn
  }
}