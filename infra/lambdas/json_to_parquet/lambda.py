import boto3
import logging
import os
import pandas as pd
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client("s3")

def lambda_handler(event, context):
    bucket_raw=event["bucket_raw"]
    bucket_stage=event["bucket_stage"]
    folder=event["folder"]

    for f in folder:
        try:
            list_keys = s3_client.list_objects(
                Bucket=bucket_raw,
                Prefix=f
            )['Contents']

            list_keys = [i['Key'] for i in list_keys]
        except Exception as e:
            logger.error("Error while listing keys.\n{}".format(e))
            raise

        df_total = pd.DataFrame()
        for i in list_keys:
            try:
                json_file = s3_client.get_object(
                    Bucket=bucket_raw,
                    Key=i,
                )['Body'].read().decode('utf-8')

                df = pd.read_json(json_file)
                df_total = df_total.append(df)
            except Exception as e:
                logger.error(
                    "Error while getting object from s3."
                    "\nError:{}\nObject{}".format(e, i))
                raise

        file_name=time.time()
        file_path=f"/tmp/{file_name}.parquet.gzip"

        try:
            df_total.to_parquet(
                path=file_path,
                engine='fastparquet',
                compression='gzip'
            )
        except Exception as e:
            logger.error(
            "Error while converting df to parquet object from s3."
            "\nError:{}\nObject{}".format(e, i))
            raise

        if f.endswith('/'):
            f = f[:-1]
        try:
            s3_client.upload_file(
                Filename=file_path,
                Bucket=bucket_stage,
                Key=f"{f}/{file_name}.parquet.gzip"
            )
        except Exception as e:
            logger.error(
            "Error while uploading file to s3."
            "\nError:{}".format(e))
            raise

        os.remove(file_path)
