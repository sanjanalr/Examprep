import boto3
import uuid

def lambda_handler(event, context):
    print("Deploy workflow verification")

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('aws-event-logs')

    item = {
        "event_id": str(uuid.uuid4()),
        "event_time": event.get("time"),
        "event_source": event.get("source"),
        "event_name": event.get("detail", {}).get("eventName"),
        "region": event.get("region"),
        "username": event.get("detail", {}).get("userIdentity", {}).get("userName", "NA"),
        "resource_name": event.get("detail", {}).get("requestParameters", {}).get("bucketName", "NA")
    }

    table.put_item(Item=item)

    return "Event stored successfully"

