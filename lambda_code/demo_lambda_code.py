import json

def lambda_handler(event, context):
    print('request:{}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type' : 'text/plain',
        },  'body':"this is a sample to use cdk and sam together"
    }

'''
Command used: "sam local invoke sam-cdk --no-event -t cdk.out/CdkSamStack.template.json"

'''