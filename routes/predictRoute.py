from flask import Flask, Blueprint, render_template, url_for, json, request, redirect
from config import MODEL_PATH
import pickle
from sklearn import datasets
from utils import saveToImage, datasets

predictRoutes = Blueprint('predict', __name__)

@predictRoutes.route('/', methods=['GET'])
def predict():
    features = [list(request.args.to_dict().values())]
    feature_cols = list(request.args.to_dict().keys())
    clf = pickle.load(open(MODEL_PATH, "rb"))
    predictResult = clf.predict(features);
    s3Url = saveToImage.save(clf, feature_cols)
    return {
        'Features': request.args.to_dict(),
        'ClassIndex': str(predictResult),
        'Classes': str(datasets.convertToClasses(predictResult)),
        'ImageUrl': s3Url
    } 
