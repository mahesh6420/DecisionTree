from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image  
import pydotplus
import boto3
import time
import os
from config import OUTPUT_PNG_PATH, AWS_ACCESS_KEY, AWS_SECRET_KEY, S3_BUCKET_NAME

def save(clf, feature_cols):
    dot_data = StringIO()
    export_graphviz(clf, out_file=dot_data,  
                    filled=True, rounded=True,
                    special_characters=True,feature_names = feature_cols)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    if os.path.exists(OUTPUT_PNG_PATH):
        os.remove(OUTPUT_PNG_PATH)
    graph.write_png(OUTPUT_PNG_PATH)
    Image(graph.create_png())
    return uploadToS3()

def uploadToS3():
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
    )
    s3 = session.resource('s3')
    key = str(time.time_ns()) + '.png'
    response = s3.meta.client.upload_file(
        Filename=OUTPUT_PNG_PATH, 
        Bucket=S3_BUCKET_NAME, 
        Key=key,
        ExtraArgs={'ACL': 'public-read'}
    )
    return 'https://'+S3_BUCKET_NAME+'.s3.us-east-2.amazonaws.com/'+key
    
