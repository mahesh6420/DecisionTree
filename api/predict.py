from flask import Flask, Blueprint, render_template, url_for, json, request, redirect
from config import MODEL_PATH
import pickle
from sklearn import datasets
from utils import saveToImage, datasets
from db.dashboard import DashboardDb

predict = Blueprint('predict', __name__)

@predict.route('/', methods=['GET'])
def predictIRIS():
    features = [list(request.args.to_dict().values())]
    feature_cols = list(request.args.to_dict().keys())
    clf = pickle.load(open(MODEL_PATH, "rb"))
    predictResult = clf.predict(features);
    s3Url = saveToImage.save(clf, feature_cols)
    resultObj = {
        'Features': request.args.to_dict(),
        'ClassIndex': predictResult.tolist(),
        'Classes': datasets.convertToClasses(predictResult),
        'ImageUrl': s3Url
    }
    DashboardDb().insertRecord(resultObj)
    return resultObj
