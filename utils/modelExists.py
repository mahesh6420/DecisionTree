from os.path import exists
from config import MODEL_PATH

def checkModelExists():
    return exists(MODEL_PATH)