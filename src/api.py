import json
from os.path import join
from werkzeug.exceptions import HTTPException
import logging
from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
import pandas as pd
import pickle
import numpy as np
import data_handler
import prediction

app = Flask(__name__)
CORS(app)

#model = pickle.load('finalized-model.pkl',mmap_mode='r')

@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


@app.route('/predict',methods=['POST'])
def predict():
    data = request.data
    req_json = json.loads(data)
    
    status_code, body = data_handler.data_handler(req_json)

    response = {
        "statusCode": status_code,
        "body": body
        }
    return response


if __name__=='__main__':
    app.run(debug=True)

