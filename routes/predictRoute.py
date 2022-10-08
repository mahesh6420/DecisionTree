from flask import Flask, Blueprint, render_template, url_for, json, request, redirect
from config import MODEL_PATH
import pickle
from utils import saveToImage

predictRoutes = Blueprint('predict', __name__)

@predictRoutes.route('/', methods=['GET'])
def predict():
    features = [list(request.args.to_dict().values())]
    feature_cols = list(request.args.to_dict().keys())
    clf = pickle.load(open(MODEL_PATH, "rb"))
    result = str(clf.predict(features)[0])
    saveToImage.save(clf, feature_cols)
    return result 
