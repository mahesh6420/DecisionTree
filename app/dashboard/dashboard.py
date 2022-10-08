from flask import Flask, Blueprint, render_template, url_for, json, request, redirect

from db.dashboard import DashboardDb

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
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
            'Classes': ", ".join(map(str, data.get('Classes'))),
            'image': data.get('ImageUrl')
        })
        count += 1
    return render_template('dashboard/index.html', rows = returnArray)
    