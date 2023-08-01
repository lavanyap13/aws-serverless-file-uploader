import json
import base64
import boto3
client=boto3.client('s3')

def lambda_handler(event, context):
    # TODO implement
    print(event)
    ms=base64.b64decode(event['body'])
    response=client.put_object(
    Body=ms,
    Bucket='demouploadfromapilambda1',
    Key='test1.png',
)
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Image uploaded Successfully')
    }
