from config import MODEL_PATH
import pickle
from sklearn import datasets
from utils import saveToImage, datasets
from db.dashboard import DashboardDb

def predictIRIS(Ifeatures):
    features = [list(Ifeatures.values())]
    feature_cols = list(Ifeatures.keys())
    clf = pickle.load(open(MODEL_PATH, "rb"))
    predictResult = clf.predict(features);
    s3Url = saveToImage.save(clf, feature_cols)
    resultObj = {
        'Features': Ifeatures,
        'ClassIndex': predictResult.tolist(),
        'Classes': datasets.convertToClasses(predictResult),
        'ImageUrl': s3Url
    }
    DashboardDb().insertRecord(resultObj)
    return resultObj