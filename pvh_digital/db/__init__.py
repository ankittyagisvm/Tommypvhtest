"""
Database module
"""

import logging
from types import SimpleNamespace

import boto3
from botocore.exceptions import ClientError
from pvh_digital import settings

log = logging.getLogger(__name__)


def get_db_resource():
    """
    Method to create connection to DynamoDB
    :return: boto3 client object to access DynamoDB
    """
    try:
        return boto3.resource(
            'dynamodb',
            region_name=settings.AWS_REGION
        )
    except ClientError as e:
        print(e.response['Error']['Message'])


def get_from_dynamo_using_id(table_name, record_id):
    """
    fetching data from dynamodb using id
    :param table_name: dynamo table name
    :param record_id: dynamo record id
    :return: record json
    """

    table = get_db_resource().Table(table_name)

    try:
        response = table.get_item(
            Key={
                'id': record_id
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


def get_all_items_from_dynamo(table_name):
    """
    Method to get all items from a dynamo table
    :param table_name: Name of the table in dynamo
    :return: json of all the items in the table
    """
    try:
        return SimpleNamespace(
            success=True, data=get_db_resource().Table(table_name).scan()['Items']
        )
    except ClientError as e:
        log.info('Unable to get data. {}'.format(e.response['Error']['Message']))
        return SimpleNamespace(success=False, error=str(e))
