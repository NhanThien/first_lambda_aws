import pandas as pd
import request
def lambda_handler(event, context):
    # TODO implement
    print ("contexttest")
    url = "https://admatic.admicro.vn/api/vietjet/campaign/report?token=BWGfpnPeoif8EKDr"
    resp = requests.get(url=url)
    data = resp.json()
    results = data["data"]
    string = "test"
    encoded_string = string.encode("utf-8")
    bucket_name = "bkt-tmp-g1-data-platform-nonprod"
    file_name = "hello_1.parquet"
    s3_path = "100001/20180223/" + file_name
    s3 = boto3.resource("s3")
    s3.Bucket(bucket_name).put_object(Key=s3_path, Body=encoded_string)
    return {
        'statusCode': 200,
        'body': json.dumps('file is created in:'+s3_path)
    }
