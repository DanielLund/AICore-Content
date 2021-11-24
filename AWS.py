# %%
from sqlalchemy import create_engine

DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
ENDPOINT = 'aicoredb.caacdab33g22.eu-west-2.rds.amazonaws.com' # Change it for your AWS endpoint
USER = 'postgres'
PASSWORD = 'postgres'
PORT = 5432
DATABASE = 'postgres'
engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")

engine.connect()

from sklearn.datasets import load_iris
import pandas as pd

data = load_iris()
iris = pd.DataFrame(data['data'], columns=data['feature_names'])
iris.head()

iris.to_sql('iris_dataset', engine, if_exists='replace')

df = pd.read_sql_table('iris_dataset', engine)
df.head()


# %%
import boto3

s3_client = boto3.client('s3')

# response = s3_client.upload_file(file_name, bucket, object_name)

s3 = boto3.resource('s3')

my_bucket = s3.Bucket('faizsbucket')

# for file in my_bucket.objects.all():
#     print(file.key)

s3_client.download_file('pokemon-sprites', 'mewtwo/front.png', 'mewtwo.png')
# %%
import requests

url = "https://faizsbucket.s3.us-east-2.amazonaws.com/cubone.png"

response = requests.get(url)
with open('cubone.png', 'wb') as f:
    f.write(response.content)
# %%

s3_client = boto3.client('s3')

dir(s3_client)

# %%
