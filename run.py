from http import client
from flask import Flask, render_template
import os
import pymongo
from routes import commonRoutes
from routes.api import predictRoute
from utils import modelExists

app = Flask(__name__, instance_relative_config=True)

# Register Routes
app.register_blueprint(commonRoutes.commonRoutes)
app.register_blueprint(predictRoute.predictRoutes,url_prefix='/predict')

# Train
if(modelExists.checkModelExists() == False):
    from core import train

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=True, host='0.0.0.0', port=port)
