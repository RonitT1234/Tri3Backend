import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from auth_middleware import token_required

from model.titanic import Titanic #imports titanic data

titanic_api = Blueprint('titanic_api', __name__,
                   url_prefix='/api/titanic')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(titanic_api)
class TitanicAPI:        
    class Predict(Resource): 
        def predict(self):
            body = request.get_json()
            # Initializing all parameters
            Pclass = body.get('Pclass')
            if age is None:
                return {'message': f'Pclass is missing'}, 400
            age = body.get('age')
            if age is None:
                return {'message': f'Age is missing'}, 400
            Sex = body.get('Sex')
            if Sex is None:
                return {'message': f'Sex is missing'}, 400
            fare = body.get('fare')
            if fare is None:
                return {'message': f'Fare is missing'}, 400
            SibSp = body.get('SibSp')
            if SibSp is None:
                return {'message': f'SibSp is missing'}, 400
            Parch = body.get('Parch')
            if Parch is None:
                return {'message': f'Parch is missing'}, 400
            
            info = [Pclass,age,Sex,SibSp,Parch,fare]
            result = Titanic.predict(info)
            
            return { 'message': result }