resource "aws_lambda_layer_version" "json_parquet" {
  filename   = "custom_layers/json_to_parquet/json2parquet.zip"
  layer_name = "json_parquet"

  compatible_runtimes = ["python3.8"]
}
