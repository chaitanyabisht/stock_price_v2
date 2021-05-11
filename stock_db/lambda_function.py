import json
import boto3

def get():
    returndict = {}
    
    client = boto3.resource('dynamodb')
    table = client.Table("Stocks")
    obj_lst = table.scan()['Items']
    
    for item in obj_lst:
        item = dict(item)
        symbol = item['Symbol']
        returndict[symbol] = {'minPrice':int(item['minPrice']), 'maxPrice':int(item['maxPrice'])}
        
    return returndict


def add(symbol,minPrice,maxPrice):
    client = boto3.resource('dynamodb')
    table = client.Table("Stocks")
    
    response = table.put_item(Item = {
        'Symbol':symbol,
        'maxPrice':maxPrice,
        'minPrice':minPrice
    })
    
    return response
    
def remove(symbol):
    client = boto3.resource('dynamodb')
    table = client.Table("Stocks")
    response = table.delete_item(Key = {'Symbol':symbol})
    return response

def lambda_handler(event, context):
    
    response = None
    
    if (event['resource'] == '/add'):
        symbol = event['queryStringParameters']['symbol']
        minPrice = event['queryStringParameters']['minPrice']
        maxPrice = event['queryStringParameters']['maxPrice']
        response = add(symbol,minPrice,maxPrice)
        
    elif (event['resource'] == '/getall'):
        response = get()
    
    elif (event['resource'] == '/remove'):
        symbol = event['queryStringParameters']['symbol']
        response = remove(symbol)
   
   
    responseObject = {}
    
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(response)
    
    return responseObject
