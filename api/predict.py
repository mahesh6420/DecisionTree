from flask import Flask, Blueprint, render_template, url_for, json, request, redirect
from core.predict import predictIRIS

predict = Blueprint('predict', __name__)

@predict.route('/', methods=['GET'])
def rPredict():
    return predictIRIS(request.args.to_dict())
