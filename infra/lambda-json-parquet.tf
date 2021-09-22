resource "aws_lambda_function" "json_to_parquet" {
  filename      = "lambdas/json_to_parquet/function.zip"
  function_name = "json_to_parquet"
  role          = aws_iam_role.s3_access.arn
  handler       = "lambda.lambda_handler"
  layers = [aws_lambda_layer_version.json_parquet.arn]
  memory_size = 256
  runtime = "python3.8"
}
