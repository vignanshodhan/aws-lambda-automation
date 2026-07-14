import json
import boto3

client = boto3.client('rds')

def lambda_handler(event, context):
    response = client.start_db_cluster(
        DBClusterIdentifier='sample-aurora-cluster'
    )
    print(response)

    return {
        'statusCode': 200,
        'body': json.dumps('RDS is starting')
    }
