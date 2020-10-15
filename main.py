import csv
import boto3

dynamodb=boto3.resource('dynamodb','us-east-1')
def read_csv(csv_file,list):
    rows=csv.DictReader(open(csv_file))
    for row in rows:
        list.append(row)


def batch_write(table_name,rows):
    table=dynamodb.Table(table_name)
    with table.batch_writer() as batch:
        for row in rows:
            batch.put_item(Item=row)
    return True


if __name__ == '__main__':
   table_name='Dynamic_SQL'
   file_name='data.csv'
   items=[]
   read_csv(file_name,items)
   status= batch_write(table_name,items)

   if (status):
       print("data sent")
   else:
       print("there was an error")