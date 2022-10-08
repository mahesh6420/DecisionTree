import os
from dotenv import load_dotenv

load_dotenv()

MODEL_PATH = 'models/model.pkl'
OUTPUT_PNG_PATH = 'app/static/tree.png'
S3_BUCKET_NAME = 'tree-image-data'
AWS_ACCESS_KEY=os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY=os.getenv('AWS_SECRET_KEY')

