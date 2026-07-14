import boto3

# Replace this value with your RDS cluster identifier
rds_cluster_identifier = 'new-cluser'

def get_rds_cluster_status(rds_client, cluster_identifier):
    response = rds_client.describe_db_clusters(DBClusterIdentifier=cluster_identifier)
    return response['DBClusters'][0]['Status']

def pause_rds_cluster(rds_client, cluster_identifier):
    rds_client.stop_db_cluster(DBClusterIdentifier=cluster_identifier)
    print(f"RDS cluster {cluster_identifier} paused.")

def resume_rds_cluster(rds_client, cluster_identifier):
    rds_client.start_db_cluster(DBClusterIdentifier=cluster_identifier)
    print(f"RDS cluster {cluster_identifier} resumed.")

def lambda_handler(event, context):
    rds_client = boto3.client('rds')
    
    status = get_rds_cluster_status(rds_client, rds_cluster_identifier)
    if status == 'available':
        pause_rds_cluster(rds_client, rds_cluster_identifier)
    elif status == 'stopped':
        resume_rds_cluster(rds_client, rds_cluster_identifier)
    else:
        print(f"Unknown status for RDS cluster {rds_cluster_identifier}: {status}")
