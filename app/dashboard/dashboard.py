from flask import Flask, Blueprint, render_template, url_for, json, request, redirect

from db.dashboard import DashboardDb
from core.predict import predictIRIS

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/', methods=['GET'])
def index():
    allData = DashboardDb().getAll()

    returnArray = []
    count = 1
    for data in allData:
        returnArray.append({
            'id': count,
            'sepal_length': data.get('Features').get('sl'),
            'sepal_width': data.get('Features').get('sw'),
            'petal_length': data.get('Features').get('pl'),
            'petal_width': data.get('Features').get('pw'),
            'ClassIndex': ", ".join(map(str, data.get('ClassIndex'))),
            'Classes': ", ".join(map(str, data.get('Classes')))
        })
        count += 1
    return render_template('dashboard/index.html', rows = returnArray)

@dashboard.route('/', methods=['POST'])
def formSubmit():
    requestDict = {
        'sl': request.form.get('sepal_length'),
        'sw': request.form.get('sepal_width'),
        'pl': request.form.get('petal_length'),
        'pw': request.form.get('petal_width')
    }
    predictIRIS(requestDict)
    return redirect(url_for('dashboard.index'))
    