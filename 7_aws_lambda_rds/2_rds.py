import urllib3
import json
import pandas as pd
import psycopg2
import os
import boto3


def lambda_handler(event, context):
    # Database Connection
    db_host = os.environ["DB_HOST"]
    db_name = os.environ["DB_NAME"]
    db_user = os.environ["DB_USER"]
    db_password = os.environ["DB_PASSWORD"]

    conn = psycopg2.connect(
        host=db_host, database=db_name, user=db_user, password=db_password
    )
    print("Connected to database")

    cursor = conn.cursor()
    table_name = "etl_utsav_stock_data"

    query = """
        CREATE TABLE IF NOT EXISTS etl_utsav_stock_data (
            identifier VARCHAR(255),
            open VARCHAR(255),
            dayHigh VARCHAR(255),
            dayLow VARCHAR(255),
            lastPrice VARCHAR(255),
            previousClose VARCHAR(255),
            change VARCHAR(255),
            pChange VARCHAR(255),
            yearHigh VARCHAR(255),
            yearLow VARCHAR(255),
            totalTradedValue VARCHAR(255),
            lastUpdateTime VARCHAR(255),
            perChange365d VARCHAR(255),
            perChange30d VARCHAR(255)
        );
        """
    cursor.execute(query)
    conn.commit()

    # Fetch Data from API
    http = urllib3.PoolManager()
    url = "https://latest-stock-price.p.rapidapi.com/any"
    headers = {
        "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
        "X-RapidAPI-Host": "latest-stock-price.p.rapidapi.com",
    }

    response = http.request("GET", url, headers=headers)
    data = response.data.decode("utf-8")
    data_json = json.loads(data)

    # # Initialize the S3 client
    # s3 = boto3.client('s3')

    # # Specify the bucket and object key
    # bucket_name = 'apprentice-training-ml-dev-utsav-raw-data'
    # object_key = 'stock_data.json'

    # # Retrieve the object from the S3 bucket
    # response = s3.get_object(Bucket=bucket_name, Key=object_key)

    # # Load the JSON data from the response
    # data_json = json.loads(response['Body'].read().decode('utf-8'))

    # Update the insert query
    insert_query = """
    INSERT INTO etl_utsav_stock_data
    (identifier, open, dayHigh, dayLow, lastPrice, previousClose, change, pChange, yearHigh, yearLow, totalTradedValue, lastUpdateTime, perChange365d, perChange30d)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    transformed_df = pd.DataFrame(data_json)
    transformed_df.drop(columns=["Volume", "symbol"], inplace=True, errors="ignore")

    # Prepare the data for insertion
    data_to_insert = [
        (
            row["identifier"],
            row["open"],
            row["dayHigh"],
            row["dayLow"],
            row["lastPrice"],
            row["previousClose"],
            row["change"],
            row["pChange"],
            row["yearHigh"],
            row["yearLow"],
            row["totalTradedValue"],
            row["lastUpdateTime"],
            row["perChange365d"],
            row["perChange30d"],
        )
        for index, row in transformed_df.iterrows()
    ]

    # Execute the insert query with the data_to_insert
    try:
        cursor.executemany(insert_query, data_to_insert)
        conn.commit()
        print("Data inserted into the database successfully.")
    except Exception as e:
        print("Error:", e)
        conn.rollback()  # Roll back the transaction in case of an error
    finally:
        cursor.close()
        conn.close()

    # Save transformed data to the second S3 bucket
    second_bucket_name = "apprentice-training-ml-dev-utsav-cleaned-data"
    second_object_key = "transformed_stock_data.json"
    s3.put_object(
        Bucket=second_bucket_name,
        Key=second_object_key,
        Body=json.dumps(transformed_data),
    )

    logger.info("Cleaned data transferred to second bucket successfully")


# Set environment variables before running this Lambda function
# RAPIDAPI_KEY
# DB_HOST
# DB_NAME
# DB_USER
# DB_PASSWORD
