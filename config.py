import os
from dotenv import load_dotenv

load_dotenv()

MODEL_PATH = 'models/model.pkl'
OUTPUT_PNG_PATH = 'static/tree.png'
MONGO_URL = os.getenv('MONGO_URL')