data "aws_lambda_function" "main" {
  function_name = "print_time"
}

resource "aws_iam_role" "main" {
  assume_role_policy = jsonencode({
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "scheduler.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy" "main" {
  policy = jsonencode({
    Statement = [
      {
        Action = "lambda:InvokeFunction"
        Effect = "Allow"
        Resource = [
          data.aws_lambda_function.main.arn
        ]
      }
    ]
  })
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