from config import MODEL_PATH
import pickle
from sklearn import datasets
from utils import datasets
from db.dashboard import DashboardDb

class PredictIRIS() :
    def __init__(self) :
        self.clf = pickle.load(open(MODEL_PATH, "rb"))

    def predictIRIS(self, Ifeatures):
        features = [list(Ifeatures.values())]
        feature_cols = list(Ifeatures.keys())
        predictResult = self.clf.predict(features);
        resultObj = {
            'Features': Ifeatures,
            'ClassIndex': predictResult.tolist(),
            'Classes': datasets.convertToClasses(predictResult)
        }
        DashboardDb().insertRecord(resultObj)
        return resultObj