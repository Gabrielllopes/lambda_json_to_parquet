# Lambda json to parquet

<img src=/img/j2p.png>

Harness the power of AWS Lambda to convert JSON files into Parquet format effortlessly. This project provides a streamlined solution for efficient data transformation, enabling seamless integration into your AWS workflows. Simplify your data processing pipeline with this Lambda-powered JSON to Parquet conversion.

## Usage example

```bash
aws lambda invoke \
--cli-binary-format raw-in-base64-out \
--function-name json_to_parquet \
--invocation-type RequestResponse \
--payload '{"bucket_raw": "test-glue-create-table-terraform-8888", "bucket_stage": "test-stage8888", "folder": ["teste_dirr/database-test/tabela_imaginaria/20-09-2021/"]}' \
response.json
```
