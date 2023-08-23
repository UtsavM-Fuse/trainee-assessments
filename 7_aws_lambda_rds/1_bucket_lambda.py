import json
import boto3
import urllib3
import os
import logging

import pandas as pd

# Initialize the S3 client
s3 = boto3.client("s3")


# first_bucket_name = os.environ['FIRST_BUCKET_NAME']
# second_bucket_name = os.environ['SECOND_BUCKET_NAME']
log_level = os.environ.get(
    "LOG_LEVEL", "INFO"
)  # 'INFO' is the default value if not set

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

data_json = dict()


def lambda_handler(event, context):
    # Fetch data from the API
    http = urllib3.PoolManager()
    url = "https://latest-stock-price.p.rapidapi.com/any"
    headers = {
        "X-RapidAPI-Key": "da39041ecamshf75624bcf3c0396p1b72b7jsn559d324f9f25",
        "X-RapidAPI-Host": "latest-stock-price.p.rapidapi.com",
    }
    response = http.request("GET", url, headers=headers)
    data = response.data.decode("utf-8")
    data_json = json.loads(data)


# Dump data into the first S3 bucket
first_bucket_name = "apprentice-training-ml-dev-utsav-raw-data"
first_object_key = "stock_data.json"
s3.put_object(
    Bucket=first_bucket_name, Key=first_object_key, Body=json.dumps(data_json)
)


# Transform data (using Pandas layer)

# Transformation logic here
transformed_data = (
    data_json.copy()
)  # Create a copy of the data to avoid modifying the original
transformed_data.dropna(how="any", inplace=True)

# Remove the key-value pair with key name "Volume"
for item in transformed_data:
    if "Volume" in item:
        del item["Volume"]

# Save transformed data to the second S3 bucket
second_bucket_name = "apprentice-training-ml-dev-utsav-cleaned-data"
second_object_key = "transformed_stock_data.json"
s3.put_object(
    Bucket=second_bucket_name, Key=second_object_key, Body=json.dumps(transformed_data)
)

logger.info("Data processing completed successfully.")
