# Lambda json to parquet

<img src=/img/j2p.png>

Uses lambda to convert json files into parquet

## Usage example

```bash
aws lambda invoke \
--cli-binary-format raw-in-base64-out \
--function-name json_to_parquet \
--invocation-type RequestResponse \
--payload '{"bucket_raw": "test-glue-create-table-terraform-8888", "bucket_stage": "test-stage8888", "folder": ["teste_dirr/database-test/tabela_imaginaria/20-09-2021/"]}' \
response.json
```