import boto3

dynamodb=boto3.resource('dynamodb','us-east-1')
def create_table(table_name):

    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  # Partition key
            },
            ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
     )
    return table
if __name__ == '__main__':
   table_name='Dynamic_SQL'

   create_table(table_name)