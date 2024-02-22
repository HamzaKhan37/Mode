from flask import Flask, request, redirect
from flask_restful import Resource, Api
from flask_cors import CORS
import os
import sys
# import predictions
# import pandas as pd
# from sklearn.preprocessing import StandardScaler
# import warnings
# from sklearn.metrics.pairwise import cosine_similarity
# from flask import Flask, jsonify
# from sklearn.cluster import KMeans
# import joblib

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

# input_data = {
#      'BMC step type': ["REVENUE STREAMS"],
#      'Problem confident': ["Fair"],
#      'Problem current progress': ["In progress - 20%"],
#      'Problem level support':["Full support required	"],
#      'Problem rate': [2],  
#      'Creator': ["hjghjkjdff@gmail.com"]
#      }

class Test(Resource):
    def get(self):
        return 'Welcome to, Test App API!'

    def post(self):
        try:
            value = request.get_json()
            if(value):
                return {'Post Values': value}, 201

            return {"error":"Invalid format."}

        except Exception as error:
            return {'error': error}

class GetPredictionOutput(Resource):
    def get(self):
        return {"error":"Invalid Method."}

    def post(self):
        try:

            data = request.get_json()
            return "Hi Every One"

        except Exception as e:
        # Handle the UnsupportedMediaType error
            return jsonify({'error': 'Unsupported media type'}), 415

api.add_resource(Test,'/')
api.add_resource(GetPredictionOutput,'/getPredictionOutput')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
