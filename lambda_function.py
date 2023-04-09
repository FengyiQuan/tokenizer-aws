import json

import preprocessing.tokenizer as tokenizer

def lambda_handler(event, context):
    # TODO implement
    message = event['message']
    function = event['function']
    if function == 'sentencizer':
        body = tokenizer.DummySentencizer(message).sentences
    elif function == 'tokenizer':
        body = tokenizer.DummyTokenizer(message).tokens
    else:
        body = 'Invalid function'
    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }