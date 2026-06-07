import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('userdata')

def lambda_handler(event, context):
    try:
        table.put_item(
            Item={
                'userId': '1',
                'name': 'Adhithyan'
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Record inserted successfully.')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
