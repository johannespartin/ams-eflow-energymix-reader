import datetime
import json
from pickletools import read_stringnl
import requests
import xml.etree.ElementTree as ET
from typing import Dict, List
import time
import boto3
from botocore.config import Config

DATABASE_NAME = "energy-mix-database"
TABLE_NAME = "energy-mix-readings-1"


def get_unix_timestamp(date_str: str, period: int) -> int:
    """
    Convert a string of the form "2022-10-27" and an integer corresponding to the
    15-minute time interval to a unix timestamp.
    This function assumes does not consider time shifts and assumes the given time zone is utc.
    """
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return int((date + datetime.timedelta(minutes=period * 15)).timestamp())


def run_query(client, query_string):
    try:
        paginator = client.get_paginator('query')
        page_iterator = paginator.paginate(QueryString=query_string)
        for page in page_iterator:
            _parse_query_result(page)
    except Exception as err:
        print("Exception while running query:", err)


def _parse_query_result(query_result):
    for a in query_result:
        rows = a['Rows']
        for row in rows: 
            print(row)
        # mix = a['energy-mix']
        # print(f"Record from {a['time']} with coal {mix['coal']} and wind {mix['wind']}")

def lambda_handler(event, context):
    session = boto3.Session()
    client = session.client('timestream-query', config=Config(read_timeout=20, max_pool_connections=5000,
                                                              retries={'max_attempts': 10}))

    run_query(client, event['query'])

    return {
        'statusCode': 200,
        'body': json.dumps('Job successful')
    }
