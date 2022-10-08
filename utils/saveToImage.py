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
