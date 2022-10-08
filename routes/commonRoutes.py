from flask import Flask, Blueprint, render_template, url_for, json, request, redirect

commonRoutes = Blueprint('common', __name__)

@commonRoutes.route('/', methods=['GET'])
def index():
    return "Hello"
    