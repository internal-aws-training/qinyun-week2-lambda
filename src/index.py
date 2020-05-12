import json
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, handler):
    object = s3.Object('aws-training-qinyun', 'BAU_Roster.csv')
    for i in object.get()['Body']._raw_stream:
        print(i.strip())
        
    copy_source = {
        'Bucket': 'aws-training-qinyun',
        'Key': 'BAU_Roster.csv'
    }
    copy_target = s3.Bucket('aws-training-qinyun-copy')
    copy_target.copy(copy_source, 'BAU_Roster_copy.csv')
    
    return {
        'statusCode': 200
    }